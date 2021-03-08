# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_sdk/protobuf/client_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sawtooth_sdk.protobuf import client_list_control_pb2 as sawtooth__sdk_dot_protobuf_dot_client__list__control__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_sdk/protobuf/client_state.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\025sawtooth.sdk.protobufP\001Z\020client_state_pb2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n(sawtooth_sdk/protobuf/client_state.proto\x1a/sawtooth_sdk/protobuf/client_list_control.proto\"\x8a\x01\n\x16\x43lientStateListRequest\x12\x12\n\nstate_root\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\x12%\n\x06paging\x18\x04 \x01(\x0b\x32\x15.ClientPagingControls\x12$\n\x07sorting\x18\x05 \x03(\x0b\x32\x13.ClientSortControls\"\x91\x03\n\x17\x43lientStateListResponse\x12/\n\x06status\x18\x01 \x01(\x0e\x32\x1f.ClientStateListResponse.Status\x12/\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\x1e.ClientStateListResponse.Entry\x12\x12\n\nstate_root\x18\x03 \x01(\t\x12%\n\x06paging\x18\x04 \x01(\x0b\x32\x15.ClientPagingResponse\x1a&\n\x05\x45ntry\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\xb0\x01\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\x0b\n\x07NO_ROOT\x10\x04\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x12\n\x0eINVALID_PAGING\x10\x06\x12\x10\n\x0cINVALID_SORT\x10\x07\x12\x13\n\x0fINVALID_ADDRESS\x10\x08\x12\x10\n\x0cINVALID_ROOT\x10\t\"<\n\x15\x43lientStateGetRequest\x12\x12\n\nstate_root\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\"\xf8\x01\n\x16\x43lientStateGetResponse\x12.\n\x06status\x18\x01 \x01(\x0e\x32\x1e.ClientStateGetResponse.Status\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x12\n\nstate_root\x18\x03 \x01(\t\"\x8a\x01\n\x06Status\x12\x10\n\x0cSTATUS_UNSET\x10\x00\x12\x06\n\x02OK\x10\x01\x12\x12\n\x0eINTERNAL_ERROR\x10\x02\x12\r\n\tNOT_READY\x10\x03\x12\x0b\n\x07NO_ROOT\x10\x04\x12\x0f\n\x0bNO_RESOURCE\x10\x05\x12\x13\n\x0fINVALID_ADDRESS\x10\x06\x12\x10\n\x0cINVALID_ROOT\x10\x07\x42+\n\x15sawtooth.sdk.protobufP\x01Z\x10\x63lient_state_pb2b\x06proto3'
  ,
  dependencies=[sawtooth__sdk_dot_protobuf_dot_client__list__control__pb2.DESCRIPTOR,])



_CLIENTSTATELISTRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientStateListResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_ROOT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_PAGING', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_SORT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ADDRESS', index=8, number=8,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ROOT', index=9, number=9,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=460,
  serialized_end=636,
)
_sym_db.RegisterEnumDescriptor(_CLIENTSTATELISTRESPONSE_STATUS)

_CLIENTSTATEGETRESPONSE_STATUS = _descriptor.EnumDescriptor(
  name='Status',
  full_name='ClientStateGetResponse.Status',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='OK', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_ERROR', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NOT_READY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_ROOT', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='NO_RESOURCE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ADDRESS', index=6, number=6,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='INVALID_ROOT', index=7, number=7,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=811,
  serialized_end=949,
)
_sym_db.RegisterEnumDescriptor(_CLIENTSTATEGETRESPONSE_STATUS)


_CLIENTSTATELISTREQUEST = _descriptor.Descriptor(
  name='ClientStateListRequest',
  full_name='ClientStateListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ClientStateListRequest.state_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='ClientStateListRequest.address', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientStateListRequest.paging', index=2,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sorting', full_name='ClientStateListRequest.sorting', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=94,
  serialized_end=232,
)


_CLIENTSTATELISTRESPONSE_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='ClientStateListResponse.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='ClientStateListResponse.Entry.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ClientStateListResponse.Entry.data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=419,
  serialized_end=457,
)

_CLIENTSTATELISTRESPONSE = _descriptor.Descriptor(
  name='ClientStateListResponse',
  full_name='ClientStateListResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientStateListResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entries', full_name='ClientStateListResponse.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ClientStateListResponse.state_root', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paging', full_name='ClientStateListResponse.paging', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_CLIENTSTATELISTRESPONSE_ENTRY, ],
  enum_types=[
    _CLIENTSTATELISTRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=235,
  serialized_end=636,
)


_CLIENTSTATEGETREQUEST = _descriptor.Descriptor(
  name='ClientStateGetRequest',
  full_name='ClientStateGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ClientStateGetRequest.state_root', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='ClientStateGetRequest.address', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=638,
  serialized_end=698,
)


_CLIENTSTATEGETRESPONSE = _descriptor.Descriptor(
  name='ClientStateGetResponse',
  full_name='ClientStateGetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ClientStateGetResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='ClientStateGetResponse.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state_root', full_name='ClientStateGetResponse.state_root', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CLIENTSTATEGETRESPONSE_STATUS,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=701,
  serialized_end=949,
)

_CLIENTSTATELISTREQUEST.fields_by_name['paging'].message_type = sawtooth__sdk_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGCONTROLS
_CLIENTSTATELISTREQUEST.fields_by_name['sorting'].message_type = sawtooth__sdk_dot_protobuf_dot_client__list__control__pb2._CLIENTSORTCONTROLS
_CLIENTSTATELISTRESPONSE_ENTRY.containing_type = _CLIENTSTATELISTRESPONSE
_CLIENTSTATELISTRESPONSE.fields_by_name['status'].enum_type = _CLIENTSTATELISTRESPONSE_STATUS
_CLIENTSTATELISTRESPONSE.fields_by_name['entries'].message_type = _CLIENTSTATELISTRESPONSE_ENTRY
_CLIENTSTATELISTRESPONSE.fields_by_name['paging'].message_type = sawtooth__sdk_dot_protobuf_dot_client__list__control__pb2._CLIENTPAGINGRESPONSE
_CLIENTSTATELISTRESPONSE_STATUS.containing_type = _CLIENTSTATELISTRESPONSE
_CLIENTSTATEGETRESPONSE.fields_by_name['status'].enum_type = _CLIENTSTATEGETRESPONSE_STATUS
_CLIENTSTATEGETRESPONSE_STATUS.containing_type = _CLIENTSTATEGETRESPONSE
DESCRIPTOR.message_types_by_name['ClientStateListRequest'] = _CLIENTSTATELISTREQUEST
DESCRIPTOR.message_types_by_name['ClientStateListResponse'] = _CLIENTSTATELISTRESPONSE
DESCRIPTOR.message_types_by_name['ClientStateGetRequest'] = _CLIENTSTATEGETREQUEST
DESCRIPTOR.message_types_by_name['ClientStateGetResponse'] = _CLIENTSTATEGETRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ClientStateListRequest = _reflection.GeneratedProtocolMessageType('ClientStateListRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTATELISTREQUEST,
  '__module__' : 'sawtooth_sdk.protobuf.client_state_pb2'
  # @@protoc_insertion_point(class_scope:ClientStateListRequest)
  })
_sym_db.RegisterMessage(ClientStateListRequest)

ClientStateListResponse = _reflection.GeneratedProtocolMessageType('ClientStateListResponse', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _CLIENTSTATELISTRESPONSE_ENTRY,
    '__module__' : 'sawtooth_sdk.protobuf.client_state_pb2'
    # @@protoc_insertion_point(class_scope:ClientStateListResponse.Entry)
    })
  ,
  'DESCRIPTOR' : _CLIENTSTATELISTRESPONSE,
  '__module__' : 'sawtooth_sdk.protobuf.client_state_pb2'
  # @@protoc_insertion_point(class_scope:ClientStateListResponse)
  })
_sym_db.RegisterMessage(ClientStateListResponse)
_sym_db.RegisterMessage(ClientStateListResponse.Entry)

ClientStateGetRequest = _reflection.GeneratedProtocolMessageType('ClientStateGetRequest', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTATEGETREQUEST,
  '__module__' : 'sawtooth_sdk.protobuf.client_state_pb2'
  # @@protoc_insertion_point(class_scope:ClientStateGetRequest)
  })
_sym_db.RegisterMessage(ClientStateGetRequest)

ClientStateGetResponse = _reflection.GeneratedProtocolMessageType('ClientStateGetResponse', (_message.Message,), {
  'DESCRIPTOR' : _CLIENTSTATEGETRESPONSE,
  '__module__' : 'sawtooth_sdk.protobuf.client_state_pb2'
  # @@protoc_insertion_point(class_scope:ClientStateGetResponse)
  })
_sym_db.RegisterMessage(ClientStateGetResponse)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
