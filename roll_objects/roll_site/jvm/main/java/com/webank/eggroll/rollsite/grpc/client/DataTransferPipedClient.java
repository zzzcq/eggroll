/*
 * Copyright 2019 The Eggroll Authors. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.webank.eggroll.rollsite.grpc.client;

import com.google.common.base.Preconditions;
import com.webank.ai.eggroll.api.core.BasicMeta;
import com.webank.ai.eggroll.api.networking.proxy.DataTransferServiceGrpc;
import com.webank.ai.eggroll.api.networking.proxy.Proxy;
import com.webank.ai.eggroll.api.networking.proxy.Proxy.Metadata;
import com.webank.ai.eggroll.api.networking.proxy.Proxy.Packet;
import com.webank.eggroll.rollsite.factory.ProxyGrpcStreamObserverFactory;
import com.webank.eggroll.rollsite.factory.ProxyGrpcStubFactory;
//import com.webank.eggroll.rollsite.factory.TransferServiceFactory;
import com.webank.eggroll.rollsite.grpc.core.api.grpc.client.GrpcAsyncClientContext;
import com.webank.eggroll.rollsite.grpc.core.api.grpc.client.GrpcStreamingClientTemplate;
import com.webank.eggroll.rollsite.grpc.core.constant.RuntimeConstants;
import com.webank.eggroll.rollsite.grpc.core.model.DelayedResult;
import com.webank.eggroll.rollsite.grpc.core.model.impl.SingleDelayedResult;
import com.webank.eggroll.rollsite.grpc.core.server.DefaultServerConf;
import com.webank.eggroll.rollsite.grpc.core.utils.ErrorUtils;
import com.webank.eggroll.rollsite.grpc.core.utils.ToStringUtils;
import com.webank.eggroll.rollsite.grpc.observer.PushClientResponseStreamObserver;
import com.webank.eggroll.rollsite.grpc.observer.UnaryCallServerRequestStreamObserver;
import com.webank.eggroll.rollsite.infra.Pipe;
import com.webank.eggroll.rollsite.infra.ResultCallback;
import com.webank.eggroll.rollsite.infra.impl.PacketQueueSingleResultPipe;
import com.webank.eggroll.rollsite.infra.impl.SingleResultCallback;
import com.webank.eggroll.rollsite.model.ProxyServerConf;
import com.webank.eggroll.rollsite.service.FdnRouter;
import io.grpc.stub.StreamObserver;
import java.lang.reflect.InvocationTargetException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import java.util.concurrent.atomic.AtomicBoolean;
import org.apache.commons.lang3.exception.ExceptionUtils;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope("prototype")
public class DataTransferPipedClient {
    private static final Logger LOGGER = LogManager.getLogger(DataTransferPipedClient.class);
    //@Autowired
    //private TransferServiceFactory transferServiceFactory;
    @Autowired
    private ProxyGrpcStubFactory proxyGrpcStubFactory;
    @Autowired
    private ProxyGrpcStreamObserverFactory proxyGrpcStreamObserverFactory;
    @Autowired
    private ProxyServerConf proxyServerConf;
    @Autowired
    private FdnRouter fdnRouter;
    @Autowired
    private ToStringUtils toStringUtils;
    @Autowired
    private ErrorUtils errorUtils;
    @Autowired
    private DefaultServerConf defaultServerConf;
    private BasicMeta.Endpoint endpoint;
    private boolean needSecureChannel;
    private long MAX_AWAIT_HOURS = 24;
    private AtomicBoolean inited = new AtomicBoolean(false);

    private Pipe pipe;

    private GrpcStreamingClientTemplate<DataTransferServiceGrpc.DataTransferServiceStub, Proxy.Packet, Proxy.Metadata> pushTemplate;

    public DataTransferPipedClient() {
        needSecureChannel = false;
    }


    public void push(Proxy.Metadata metadata, Pipe pipe) {
        String onelineStringMetadata = toStringUtils.toOneLineString(metadata);
        LOGGER.info("[PUSH][CLIENT] client send push to server: {}",
            onelineStringMetadata);
        DataTransferServiceGrpc.DataTransferServiceStub stub = getStub(metadata.getSrc(), metadata.getDst());

        try {
            Proxy.Topic from = metadata.getSrc();
            Proxy.Topic to = metadata.getDst();
            stub = getStub(from, to);
        } catch (Exception e) {
            LOGGER.error("[PUSH][CLIENT] error when creating push stub");
            pipe.onError(e);
        }

        final CountDownLatch finishLatch = new CountDownLatch(1);
        final ResultCallback<Metadata> resultCallback = new SingleResultCallback<Metadata>();

        StreamObserver<Proxy.Metadata> responseObserver =
            proxyGrpcStreamObserverFactory.createClientPushResponseStreamObserver(resultCallback, finishLatch);

        StreamObserver<Proxy.Packet> requestObserver = stub.push(responseObserver);
        LOGGER.info("[PUSH][CLIENT] push stub: {}, metadata: {}",
            stub.getChannel(), onelineStringMetadata);

        int emptyRetryCount = 0;
        Proxy.Packet packet = null;
        do {
            //packet = (Proxy.Packet) pipe.read(1, TimeUnit.SECONDS);
            packet = (Proxy.Packet) pipe.read();

            if (packet != null) {
                requestObserver.onNext(packet);
                emptyRetryCount = 0;
            } else {
                ++emptyRetryCount;
                if (emptyRetryCount % 60 == 0) {
                    LOGGER.info("[PUSH][CLIENT] push stub waiting. empty retry count: {}, metadata: {}",
                        emptyRetryCount, onelineStringMetadata);
                }
            }
        } while ((packet != null || !pipe.isDrained()) && emptyRetryCount < 30 && !pipe.hasError());

        LOGGER.info("[PUSH][CLIENT] break out from loop. Proxy.Packet is null? {} ; pipe.isDrained()? {}" +
                ", pipe.hasError? {}, metadata: {}",
            packet == null, pipe.isDrained(), pipe.hasError(), onelineStringMetadata);

        if (pipe.hasError()) {
            Throwable error = pipe.getError();
            LOGGER.error("[PUSH][CLIENT] push error: {}, metadata: {}",
                ExceptionUtils.getStackTrace(error), onelineStringMetadata);
            requestObserver.onError(error);

            return;
        }

        requestObserver.onCompleted();
        try {
            finishLatch.await(MAX_AWAIT_HOURS, TimeUnit.HOURS);
        } catch (InterruptedException e) {
            LOGGER.error("[PUSH][CLIENT] client push: finishLatch.await() interrupted");
            requestObserver.onError(errorUtils.toGrpcRuntimeException(e));
            pipe.onError(e);
            Thread.currentThread().interrupt();
            return;
        }

        if (pipe instanceof PacketQueueSingleResultPipe) {
            PacketQueueSingleResultPipe convertedPipe = (PacketQueueSingleResultPipe) pipe;
            if (resultCallback.hasResult()) {
                convertedPipe.setResult(resultCallback.getResult());
            } else {
                LOGGER.warn("No Proxy.Metadata returned in pipe. request metadata: {}",
                    onelineStringMetadata);
            }
        }
        pipe.onComplete();

        LOGGER.info("[PUSH][CLIENT] push closing pipe. metadata: {}",
            onelineStringMetadata);
    }


    //public synchronized void initPush(TransferBroker request, BasicMeta.Endpoint endpoint) {
    public synchronized void initPush(Proxy.Metadata metadata, Pipe pipe) {
        //LOGGER.info("[DEBUG][CLUSTERCOMM] initPush. broker: {}, transferMetaId: {}", pipe, toStringUtils.toOneLineString(request.getTransferMeta()));
        /*
        GrpcAsyncClientContext<DataTransferServiceGrpc.DataTransferServiceStub, Proxy.Packet, Proxy.Metadata> asyncClientContext
            = transferServiceFactory.createPushClientGrpcAsyncClientContext();

        //BasicMeta.Endpoint.Builder builder = BasicMeta.Endpoint.newBuilder();
        endpoint = proxyGrpcStubFactory.getAsyncEndpoint(metadata.getDst());
        //endpoint = builder.setIp("192.168.1.101").setPort(9395).build();

        asyncClientContext.setLatchInitCount(1)
            .setEndpoint(endpoint)
            .setSecureRequest(defaultServerConf.isSecureClient())
            .setFinishTimeout(RuntimeConstants.DEFAULT_WAIT_TIME, RuntimeConstants.DEFAULT_TIMEUNIT)
            .setCallerStreamingMethodInvoker(DataTransferServiceGrpc.DataTransferServiceStub::push)
            .setCallerStreamObserverClassAndArguments(PushClientResponseStreamObserver.class, pipe)
            .setRequestStreamProcessorClassAndArguments(PushStreamProcessor.class, pipe);

        pushTemplate = transferServiceFactory.createPushClientTemplate();
        pushTemplate.setGrpcAsyncClientContext(asyncClientContext);

        pushTemplate.initCallerStreamingRpc();

        inited.compareAndSet(false, true);
        */
    }

    public void doPush() {
        if (pushTemplate == null) {
            throw new IllegalStateException("pushTemplate has not been initialized yet");
        }

        while (!inited.get()) {
            LOGGER.info("[DEBUG][CLUSTERCOMM] proxyClient not inited yet");

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                LOGGER.error("error in doPush: " + ExceptionUtils.getStackTrace(e));
                Thread.currentThread().interrupt();
            }
        }
        LOGGER.info("[DEBUG][CLUSTERCOMM] doPush call processCallerStreamingRpc");
        pushTemplate.processCallerStreamingRpc();
    }

    public synchronized void completePush() {
        // LOGGER.info("[PUSH][CLIENT] completing push");
        if (pushTemplate == null) {
            throw new IllegalStateException("pushTemplate has not been initialized yet");
        }
        pushTemplate.completeStreamingRpc();
    }

    public void pull(Proxy.Metadata metadata, Pipe pipe) {
        String onelineStringMetadata = toStringUtils.toOneLineString(metadata);
        LOGGER.info("[PULL][CLIENT] client send pull to server: {}", onelineStringMetadata);
        DataTransferServiceGrpc.DataTransferServiceStub stub = getStub(metadata.getDst(), metadata.getSrc());

        final CountDownLatch finishLatch = new CountDownLatch(1);

        StreamObserver<Proxy.Packet> responseObserver =
                proxyGrpcStreamObserverFactory.createClientPullResponseStreamObserver(pipe, finishLatch, metadata);

        stub.pull(metadata, responseObserver);
        LOGGER.info("[PULL][CLIENT] pull stub: {}, metadata: {}",
                stub.getChannel(), onelineStringMetadata);

        try {
            finishLatch.await(MAX_AWAIT_HOURS, TimeUnit.HOURS);
        } catch (InterruptedException e) {
            LOGGER.error("[PULL][CLIENT] client pull: finishLatch.await() interrupted");
            responseObserver.onError(errorUtils.toGrpcRuntimeException(e));
            pipe.onError(e);
            Thread.currentThread().interrupt();
            return;
        }

        responseObserver.onCompleted();
    }

    public void unaryCall_(Proxy.Packet packet, Pipe pipe) {
        Preconditions.checkNotNull(packet);
        Proxy.Metadata header = packet.getHeader();
        String onelineStringMetadata = toStringUtils.toOneLineString(header);
        LOGGER.info("[UNARYCALL][CLIENT] client send unary call to server: {}", onelineStringMetadata);
        //LOGGER.info("[UNARYCALL][CLIENT] packet: {}", toStringUtils.toOneLineString(packet));

        DataTransferServiceGrpc.DataTransferServiceStub stub = getStub(
                packet.getHeader().getSrc(), packet.getHeader().getDst());

        final CountDownLatch finishLatch = new CountDownLatch(1);
        StreamObserver<Proxy.Packet> responseObserver = proxyGrpcStreamObserverFactory
                .createClientUnaryCallResponseStreamObserver(pipe, finishLatch, packet.getHeader());
        stub.unaryCall(packet, responseObserver);

        LOGGER.info("[UNARYCALL][CLIENT] unary call stub: {}, metadata: {}",
                stub.getChannel(), onelineStringMetadata);

        try {
            finishLatch.await(MAX_AWAIT_HOURS, TimeUnit.HOURS);
        } catch (InterruptedException e) {
            LOGGER.error("[UNARYCALL][CLIENT] client unary call: finishLatch.await() interrupted");
            responseObserver.onError(errorUtils.toGrpcRuntimeException(e));
            pipe.onError(e);
            Thread.currentThread().interrupt();
            return;
        }

        responseObserver.onCompleted();
    }

    public Proxy.Packet unaryCall(Proxy.Packet request, Pipe pipe) {
        /*
        DelayedResult<Packet> delayedResult = new SingleDelayedResult<>();
        GrpcAsyncClientContext<DataTransferServiceGrpc.DataTransferServiceStub, Proxy.Packet, Proxy.Packet> context
            = transferServiceFactory.createUnaryCallClientGrpcAsyncClientContext();

        BasicMeta.Endpoint.Builder builder = BasicMeta.Endpoint.newBuilder();
        endpoint = builder.setIp("localhost").setPort(8888).build();

        context.setLatchInitCount(1)
            .setEndpoint(endpoint)
            .setSecureRequest(defaultServerConf.isSecureClient())
            .setFinishTimeout(RuntimeConstants.DEFAULT_WAIT_TIME, RuntimeConstants.DEFAULT_TIMEUNIT)
            .setCalleeStreamingMethodInvoker(DataTransferServiceGrpc.DataTransferServiceStub::unaryCall)
            .setCallerStreamObserverClassAndArguments(UnaryCallServerRequestStreamObserver.class, delayedResult);

        GrpcStreamingClientTemplate<DataTransferServiceGrpc.DataTransferServiceStub, Proxy.Packet, Proxy.Packet> template
            = transferServiceFactory.createUnaryCallClientTemplate();
        template.setGrpcAsyncClientContext(context);
        */
        Proxy.Packet result = null;
        /*
        try {
            result = template.calleeStreamingRpcWithImmediateDelayedResult(request, delayedResult);
        } catch (InvocationTargetException e) {
            throw new RuntimeException(e);
        }
        */
        return result;

    }

    private DataTransferServiceGrpc.DataTransferServiceStub getStub(Proxy.Topic from, Proxy.Topic to) {
        if (endpoint == null && !fdnRouter.isAllowed(from, to)) {
            throw new SecurityException("no permission from " + toStringUtils.toOneLineString(from)
                    + " to " + toStringUtils.toOneLineString(to));
        }

        DataTransferServiceGrpc.DataTransferServiceStub stub = null;
        if (endpoint == null) {
            stub = proxyGrpcStubFactory.getAsyncStub(to);
        } else {
            stub = proxyGrpcStubFactory.getAsyncStub(endpoint);
        }

        LOGGER.info("[ROUTE] route info: {} routed to {}", toStringUtils.toOneLineString(to),
                toStringUtils.toOneLineString(fdnRouter.route(to)));

        fdnRouter.route(from);

        return stub;
    }

    public boolean isNeedSecureChannel() {
        return needSecureChannel;
    }

    public void setNeedSecureChannel(boolean needSecureChannel) {
        this.needSecureChannel = needSecureChannel;
    }

    public BasicMeta.Endpoint getEndpoint() {
        return endpoint;
    }

    public void setEndpoint(BasicMeta.Endpoint endpoint) {
        this.endpoint = endpoint;
    }
}
