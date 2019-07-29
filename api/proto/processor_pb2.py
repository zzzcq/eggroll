# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: processor.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import kv_pb2 as kv__pb2
import storage_basic_pb2 as storage__basic__pb2
import basic_meta_pb2 as basic__meta__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='processor.proto',
  package='com.webank.ai.eggroll.api.computing.processor',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0fprocessor.proto\x12-com.webank.ai.eggroll.api.computing.processor\x1a\x08kv.proto\x1a\x13storage-basic.proto\x1a\x10\x62\x61sic-meta.proto\"#\n\x0bProcessConf\x12\x14\n\x0cnamingPolicy\x18\x01 \x01(\t\"}\n\x08TaskInfo\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x13\n\x0b\x66unction_id\x18\x02 \x01(\t\x12\x16\n\x0e\x66unction_bytes\x18\x03 \x01(\x0c\x12\x1a\n\x12isInPlaceComputing\x18\x04 \x01(\x08\x12\x17\n\x0f\x63omputingEngine\x18\x05 \x01(\t\"\xa1\x02\n\x0cUnaryProcess\x12\x45\n\x04info\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.eggroll.api.computing.processor.TaskInfo\x12\x42\n\x07operand\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12H\n\x04\x63onf\x18\x03 \x01(\x0b\x32:.com.webank.ai.eggroll.api.computing.processor.ProcessConf\x12<\n\x07session\x18\x14 \x01(\x0b\x32+.com.webank.ai.eggroll.api.core.SessionInfo\"\xe1\x02\n\rBinaryProcess\x12\x45\n\x04info\x18\x01 \x01(\x0b\x32\x37.com.webank.ai.eggroll.api.computing.processor.TaskInfo\x12?\n\x04left\x18\x02 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12@\n\x05right\x18\x03 \x01(\x0b\x32\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12H\n\x04\x63onf\x18\x04 \x01(\x0b\x32:.com.webank.ai.eggroll.api.computing.processor.ProcessConf\x12<\n\x07session\x18\x14 \x01(\x0b\x32+.com.webank.ai.eggroll.api.core.SessionInfo2\xd7\n\n\x0eProcessService\x12u\n\x03map\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12{\n\tmapValues\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12w\n\x04join\x12<.com.webank.ai.eggroll.api.computing.processor.BinaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12s\n\x06reduce\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a*.com.webank.ai.eggroll.api.storage.Operand0\x01\x12\x7f\n\rmapPartitions\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12v\n\x04glom\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12x\n\x06sample\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12\x80\x01\n\rsubtractByKey\x12<.com.webank.ai.eggroll.api.computing.processor.BinaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12x\n\x06\x66ilter\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12x\n\x05union\x12<.com.webank.ai.eggroll.api.computing.processor.BinaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocator\x12y\n\x07\x66latMap\x12;.com.webank.ai.eggroll.api.computing.processor.UnaryProcess\x1a\x31.com.webank.ai.eggroll.api.storage.StorageLocatorb\x06proto3')
  ,
  dependencies=[kv__pb2.DESCRIPTOR,storage__basic__pb2.DESCRIPTOR,basic__meta__pb2.DESCRIPTOR,])




_PROCESSCONF = _descriptor.Descriptor(
  name='ProcessConf',
  full_name='com.webank.ai.eggroll.api.computing.processor.ProcessConf',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='namingPolicy', full_name='com.webank.ai.eggroll.api.computing.processor.ProcessConf.namingPolicy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=150,
)


_TASKINFO = _descriptor.Descriptor(
  name='TaskInfo',
  full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_id', full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo.task_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_id', full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo.function_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='function_bytes', full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo.function_bytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isInPlaceComputing', full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo.isInPlaceComputing', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='computingEngine', full_name='com.webank.ai.eggroll.api.computing.processor.TaskInfo.computingEngine', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=277,
)


_UNARYPROCESS = _descriptor.Descriptor(
  name='UnaryProcess',
  full_name='com.webank.ai.eggroll.api.computing.processor.UnaryProcess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='com.webank.ai.eggroll.api.computing.processor.UnaryProcess.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='operand', full_name='com.webank.ai.eggroll.api.computing.processor.UnaryProcess.operand', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='com.webank.ai.eggroll.api.computing.processor.UnaryProcess.conf', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session', full_name='com.webank.ai.eggroll.api.computing.processor.UnaryProcess.session', index=3,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=280,
  serialized_end=569,
)


_BINARYPROCESS = _descriptor.Descriptor(
  name='BinaryProcess',
  full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='info', full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess.info', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess.left', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess.right', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='conf', full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess.conf', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='session', full_name='com.webank.ai.eggroll.api.computing.processor.BinaryProcess.session', index=4,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=572,
  serialized_end=925,
)

_UNARYPROCESS.fields_by_name['info'].message_type = _TASKINFO
_UNARYPROCESS.fields_by_name['operand'].message_type = storage__basic__pb2._STORAGELOCATOR
_UNARYPROCESS.fields_by_name['conf'].message_type = _PROCESSCONF
_UNARYPROCESS.fields_by_name['session'].message_type = basic__meta__pb2._SESSIONINFO
_BINARYPROCESS.fields_by_name['info'].message_type = _TASKINFO
_BINARYPROCESS.fields_by_name['left'].message_type = storage__basic__pb2._STORAGELOCATOR
_BINARYPROCESS.fields_by_name['right'].message_type = storage__basic__pb2._STORAGELOCATOR
_BINARYPROCESS.fields_by_name['conf'].message_type = _PROCESSCONF
_BINARYPROCESS.fields_by_name['session'].message_type = basic__meta__pb2._SESSIONINFO
DESCRIPTOR.message_types_by_name['ProcessConf'] = _PROCESSCONF
DESCRIPTOR.message_types_by_name['TaskInfo'] = _TASKINFO
DESCRIPTOR.message_types_by_name['UnaryProcess'] = _UNARYPROCESS
DESCRIPTOR.message_types_by_name['BinaryProcess'] = _BINARYPROCESS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProcessConf = _reflection.GeneratedProtocolMessageType('ProcessConf', (_message.Message,), dict(
  DESCRIPTOR = _PROCESSCONF,
  __module__ = 'processor_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.computing.processor.ProcessConf)
  ))
_sym_db.RegisterMessage(ProcessConf)

TaskInfo = _reflection.GeneratedProtocolMessageType('TaskInfo', (_message.Message,), dict(
  DESCRIPTOR = _TASKINFO,
  __module__ = 'processor_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.computing.processor.TaskInfo)
  ))
_sym_db.RegisterMessage(TaskInfo)

UnaryProcess = _reflection.GeneratedProtocolMessageType('UnaryProcess', (_message.Message,), dict(
  DESCRIPTOR = _UNARYPROCESS,
  __module__ = 'processor_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.computing.processor.UnaryProcess)
  ))
_sym_db.RegisterMessage(UnaryProcess)

BinaryProcess = _reflection.GeneratedProtocolMessageType('BinaryProcess', (_message.Message,), dict(
  DESCRIPTOR = _BINARYPROCESS,
  __module__ = 'processor_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.eggroll.api.computing.processor.BinaryProcess)
  ))
_sym_db.RegisterMessage(BinaryProcess)



_PROCESSSERVICE = _descriptor.ServiceDescriptor(
  name='ProcessService',
  full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=928,
  serialized_end=2295,
  methods=[
  _descriptor.MethodDescriptor(
    name='map',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.map',
    index=0,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='mapValues',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.mapValues',
    index=1,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='join',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.join',
    index=2,
    containing_service=None,
    input_type=_BINARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='reduce',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.reduce',
    index=3,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=kv__pb2._OPERAND,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='mapPartitions',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.mapPartitions',
    index=4,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='glom',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.glom',
    index=5,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='sample',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.sample',
    index=6,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='subtractByKey',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.subtractByKey',
    index=7,
    containing_service=None,
    input_type=_BINARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='filter',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.filter',
    index=8,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='union',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.union',
    index=9,
    containing_service=None,
    input_type=_BINARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='flatMap',
    full_name='com.webank.ai.eggroll.api.computing.processor.ProcessService.flatMap',
    index=10,
    containing_service=None,
    input_type=_UNARYPROCESS,
    output_type=storage__basic__pb2._STORAGELOCATOR,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROCESSSERVICE)

DESCRIPTOR.services_by_name['ProcessService'] = _PROCESSSERVICE

# @@protoc_insertion_point(module_scope)
