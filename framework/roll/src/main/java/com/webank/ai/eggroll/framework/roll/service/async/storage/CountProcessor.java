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

package com.webank.ai.eggroll.framework.roll.service.async.storage;

import com.webank.ai.eggroll.api.storage.Kv;
import com.webank.ai.eggroll.core.io.StoreInfo;
import com.webank.ai.eggroll.framework.meta.service.dao.generated.model.model.Node;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Component;

@Component
@Scope("prototype")
public class CountProcessor extends BaseStorageProcessor<Kv.Empty, Kv.Count> {

    public CountProcessor(Kv.Empty request, StoreInfo storeInfo, Node node) {
        super(request, storeInfo, node);
    }

    @Override
    public Kv.Count call() throws Exception {
        Kv.Count result = storageServiceClient.count(request, storeInfo, node);

        return result;
    }
}
