# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sawtooth_sdk/protobuf/events.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sawtooth_sdk/protobuf/events.proto',
  package='',
  syntax='proto3',
  serialized_options=b'\n\025sawtooth.sdk.protobufP\001Z\nevents_pb2',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\"sawtooth_sdk/protobuf/events.proto\"x\n\x05\x45vent\x12\x12\n\nevent_type\x18\x01 \x01(\t\x12$\n\nattributes\x18\x02 \x03(\x0b\x32\x10.Event.Attribute\x12\x0c\n\x04\x64\x61ta\x18\x03 \x01(\x0c\x1a\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"#\n\tEventList\x12\x16\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x06.Event\"\xc1\x01\n\x0b\x45ventFilter\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x14\n\x0cmatch_string\x18\x02 \x01(\t\x12,\n\x0b\x66ilter_type\x18\x03 \x01(\x0e\x32\x17.EventFilter.FilterType\"a\n\nFilterType\x12\x15\n\x11\x46ILTER_TYPE_UNSET\x10\x00\x12\x0e\n\nSIMPLE_ANY\x10\x01\x12\x0e\n\nSIMPLE_ALL\x10\x02\x12\r\n\tREGEX_ANY\x10\x03\x12\r\n\tREGEX_ALL\x10\x04\"F\n\x11\x45ventSubscription\x12\x12\n\nevent_type\x18\x01 \x01(\t\x12\x1d\n\x07\x66ilters\x18\x02 \x03(\x0b\x32\x0c.EventFilterB%\n\x15sawtooth.sdk.protobufP\x01Z\nevents_pb2b\x06proto3'
)



_EVENTFILTER_FILTERTYPE = _descriptor.EnumDescriptor(
  name='FilterType',
  full_name='EventFilter.FilterType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FILTER_TYPE_UNSET', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_ANY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SIMPLE_ALL', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REGEX_ANY', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='REGEX_ALL', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=294,
  serialized_end=391,
)
_sym_db.RegisterEnumDescriptor(_EVENTFILTER_FILTERTYPE)


_EVENT_ATTRIBUTE = _descriptor.Descriptor(
  name='Attribute',
  full_name='Event.Attribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Event.Attribute.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='Event.Attribute.value', index=1,
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
  serialized_start=119,
  serialized_end=158,
)

_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='Event.event_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='Event.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='Event.data', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_EVENT_ATTRIBUTE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=158,
)


_EVENTLIST = _descriptor.Descriptor(
  name='EventList',
  full_name='EventList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='EventList.events', index=0,
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
  serialized_start=160,
  serialized_end=195,
)


_EVENTFILTER = _descriptor.Descriptor(
  name='EventFilter',
  full_name='EventFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='EventFilter.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='match_string', full_name='EventFilter.match_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filter_type', full_name='EventFilter.filter_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENTFILTER_FILTERTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=391,
)


_EVENTSUBSCRIPTION = _descriptor.Descriptor(
  name='EventSubscription',
  full_name='EventSubscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='event_type', full_name='EventSubscription.event_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='filters', full_name='EventSubscription.filters', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=393,
  serialized_end=463,
)

_EVENT_ATTRIBUTE.containing_type = _EVENT
_EVENT.fields_by_name['attributes'].message_type = _EVENT_ATTRIBUTE
_EVENTLIST.fields_by_name['events'].message_type = _EVENT
_EVENTFILTER.fields_by_name['filter_type'].enum_type = _EVENTFILTER_FILTERTYPE
_EVENTFILTER_FILTERTYPE.containing_type = _EVENTFILTER
_EVENTSUBSCRIPTION.fields_by_name['filters'].message_type = _EVENTFILTER
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['EventList'] = _EVENTLIST
DESCRIPTOR.message_types_by_name['EventFilter'] = _EVENTFILTER
DESCRIPTOR.message_types_by_name['EventSubscription'] = _EVENTSUBSCRIPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), {

  'Attribute' : _reflection.GeneratedProtocolMessageType('Attribute', (_message.Message,), {
    'DESCRIPTOR' : _EVENT_ATTRIBUTE,
    '__module__' : 'sawtooth_sdk.protobuf.events_pb2'
    # @@protoc_insertion_point(class_scope:Event.Attribute)
    })
  ,
  'DESCRIPTOR' : _EVENT,
  '__module__' : 'sawtooth_sdk.protobuf.events_pb2'
  # @@protoc_insertion_point(class_scope:Event)
  })
_sym_db.RegisterMessage(Event)
_sym_db.RegisterMessage(Event.Attribute)

EventList = _reflection.GeneratedProtocolMessageType('EventList', (_message.Message,), {
  'DESCRIPTOR' : _EVENTLIST,
  '__module__' : 'sawtooth_sdk.protobuf.events_pb2'
  # @@protoc_insertion_point(class_scope:EventList)
  })
_sym_db.RegisterMessage(EventList)

EventFilter = _reflection.GeneratedProtocolMessageType('EventFilter', (_message.Message,), {
  'DESCRIPTOR' : _EVENTFILTER,
  '__module__' : 'sawtooth_sdk.protobuf.events_pb2'
  # @@protoc_insertion_point(class_scope:EventFilter)
  })
_sym_db.RegisterMessage(EventFilter)

EventSubscription = _reflection.GeneratedProtocolMessageType('EventSubscription', (_message.Message,), {
  'DESCRIPTOR' : _EVENTSUBSCRIPTION,
  '__module__' : 'sawtooth_sdk.protobuf.events_pb2'
  # @@protoc_insertion_point(class_scope:EventSubscription)
  })
_sym_db.RegisterMessage(EventSubscription)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
