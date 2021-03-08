# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_sdk/protobuf/identity.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_sdk/protobuf/identity.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\032sawtooth.identity.protobufP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$sawtooth_sdk/protobuf/identity.proto\"\xae\x01\n\x06Policy\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1e\n\x07\x65ntries\x18\x02 \x03(\x0b\x32\r.Policy.Entry\x1a\x35\n\x05\x45ntry\x12\x1f\n\x04type\x18\x01 \x01(\x0e\x32\x11.Policy.EntryType\x12\x0b\n\x03key\x18\x02 \x01(\t\"?\n\tEntryType\x12\x14\n\x10\x45NTRY_TYPE_UNSET\x10\x00\x12\x0e\n\nPERMIT_KEY\x10\x01\x12\x0c\n\x08\x44\x45NY_KEY\x10\x02\"\'\n\nPolicyList\x12\x19\n\x08policies\x18\x01 \x03(\x0b\x32\x07.Policy\")\n\x04Role\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0bpolicy_name\x18\x02 \x01(\t\" \n\x08RoleList\x12\x14\n\x05roles\x18\x01 \x03(\x0b\x32\x05.RoleB\x1e\n\x1asawtooth.identity.protobufP\x01\x62\x06proto3'
)



_POLICY_ENTRYTYPE = _descriptor.EnumDescriptor(
  name='EntryType',
  full_name='Policy.EntryType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTRY_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PERMIT_KEY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DENY_KEY', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=152,
  serialized_end=215,
)
_sym_db.RegisterEnumDescriptor(_POLICY_ENTRYTYPE)


_POLICY_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='Policy.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Policy.Entry.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='Policy.Entry.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=97,
  serialized_end=150,
)

_POLICY = _descriptor.Descriptor(
  name='Policy',
  full_name='Policy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Policy.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='entries', full_name='Policy.entries', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_POLICY_ENTRY, ],
  enum_types=[
    _POLICY_ENTRYTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=215,
)


_POLICYLIST = _descriptor.Descriptor(
  name='PolicyList',
  full_name='PolicyList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='policies', full_name='PolicyList.policies', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=217,
  serialized_end=256,
)


_ROLE = _descriptor.Descriptor(
  name='Role',
  full_name='Role',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Role.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='policy_name', full_name='Role.policy_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=258,
  serialized_end=299,
)


_ROLELIST = _descriptor.Descriptor(
  name='RoleList',
  full_name='RoleList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='roles', full_name='RoleList.roles', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=301,
  serialized_end=333,
)

_POLICY_ENTRY.fields_by_name['type'].enum_type = _POLICY_ENTRYTYPE
_POLICY_ENTRY.containing_type = _POLICY
_POLICY.fields_by_name['entries'].message_type = _POLICY_ENTRY
_POLICY_ENTRYTYPE.containing_type = _POLICY
_POLICYLIST.fields_by_name['policies'].message_type = _POLICY
_ROLELIST.fields_by_name['roles'].message_type = _ROLE
DESCRIPTOR.message_types_by_name['Policy'] = _POLICY
DESCRIPTOR.message_types_by_name['PolicyList'] = _POLICYLIST
DESCRIPTOR.message_types_by_name['Role'] = _ROLE
DESCRIPTOR.message_types_by_name['RoleList'] = _ROLELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Policy = _reflection.GeneratedProtocolMessageType('Policy', (_message.Message,), {

  'Entry' : _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
    'DESCRIPTOR' : _POLICY_ENTRY,
    '__module__' : 'sawtooth_sdk.protobuf.identity_pb2'
    # @@protoc_insertion_point(class_scope:Policy.Entry)
    })
  ,
  'DESCRIPTOR' : _POLICY,
  '__module__' : 'sawtooth_sdk.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:Policy)
  })
_sym_db.RegisterMessage(Policy)
_sym_db.RegisterMessage(Policy.Entry)

PolicyList = _reflection.GeneratedProtocolMessageType('PolicyList', (_message.Message,), {
  'DESCRIPTOR' : _POLICYLIST,
  '__module__' : 'sawtooth_sdk.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:PolicyList)
  })
_sym_db.RegisterMessage(PolicyList)

Role = _reflection.GeneratedProtocolMessageType('Role', (_message.Message,), {
  'DESCRIPTOR' : _ROLE,
  '__module__' : 'sawtooth_sdk.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:Role)
  })
_sym_db.RegisterMessage(Role)

RoleList = _reflection.GeneratedProtocolMessageType('RoleList', (_message.Message,), {
  'DESCRIPTOR' : _ROLELIST,
  '__module__' : 'sawtooth_sdk.protobuf.identity_pb2'
  # @@protoc_insertion_point(class_scope:RoleList)
  })
_sym_db.RegisterMessage(RoleList)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
