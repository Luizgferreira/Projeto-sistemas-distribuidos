# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authentication.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='authentication.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x61uthentication.proto\"\'\n\x05Login\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"\x19\n\x06\x41nswer\x12\x0f\n\x07is_auth\x18\x01 \x01(\x08\"0\n\tAuthorize\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nvehicle_id\x18\x02 \x01(\x05\"<\n\x06\x46inish\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x12\n\nvehicle_id\x18\x02 \x01(\x05\x12\r\n\x05tempo\x18\x03 \x01(\x02\x32\x7f\n\x0e\x41uthentication\x12\x1e\n\tmakelogin\x12\x06.Login\x1a\x07.Answer\"\x00\x12*\n\x11\x61uthorize_vehicle\x12\n.Authorize\x1a\x07.Answer\"\x00\x12!\n\x0buser_finish\x12\x07.Finish\x1a\x07.Answer\"\x00\x62\x06proto3')
)




_LOGIN = _descriptor.Descriptor(
  name='Login',
  full_name='Login',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Login.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='Login.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=24,
  serialized_end=63,
)


_ANSWER = _descriptor.Descriptor(
  name='Answer',
  full_name='Answer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_auth', full_name='Answer.is_auth', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=65,
  serialized_end=90,
)


_AUTHORIZE = _descriptor.Descriptor(
  name='Authorize',
  full_name='Authorize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Authorize.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_id', full_name='Authorize.vehicle_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=92,
  serialized_end=140,
)


_FINISH = _descriptor.Descriptor(
  name='Finish',
  full_name='Finish',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='Finish.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vehicle_id', full_name='Finish.vehicle_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tempo', full_name='Finish.tempo', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=142,
  serialized_end=202,
)

DESCRIPTOR.message_types_by_name['Login'] = _LOGIN
DESCRIPTOR.message_types_by_name['Answer'] = _ANSWER
DESCRIPTOR.message_types_by_name['Authorize'] = _AUTHORIZE
DESCRIPTOR.message_types_by_name['Finish'] = _FINISH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Login = _reflection.GeneratedProtocolMessageType('Login', (_message.Message,), {
  'DESCRIPTOR' : _LOGIN,
  '__module__' : 'authentication_pb2'
  # @@protoc_insertion_point(class_scope:Login)
  })
_sym_db.RegisterMessage(Login)

Answer = _reflection.GeneratedProtocolMessageType('Answer', (_message.Message,), {
  'DESCRIPTOR' : _ANSWER,
  '__module__' : 'authentication_pb2'
  # @@protoc_insertion_point(class_scope:Answer)
  })
_sym_db.RegisterMessage(Answer)

Authorize = _reflection.GeneratedProtocolMessageType('Authorize', (_message.Message,), {
  'DESCRIPTOR' : _AUTHORIZE,
  '__module__' : 'authentication_pb2'
  # @@protoc_insertion_point(class_scope:Authorize)
  })
_sym_db.RegisterMessage(Authorize)

Finish = _reflection.GeneratedProtocolMessageType('Finish', (_message.Message,), {
  'DESCRIPTOR' : _FINISH,
  '__module__' : 'authentication_pb2'
  # @@protoc_insertion_point(class_scope:Finish)
  })
_sym_db.RegisterMessage(Finish)



_AUTHENTICATION = _descriptor.ServiceDescriptor(
  name='Authentication',
  full_name='Authentication',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=204,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='makelogin',
    full_name='Authentication.makelogin',
    index=0,
    containing_service=None,
    input_type=_LOGIN,
    output_type=_ANSWER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='authorize_vehicle',
    full_name='Authentication.authorize_vehicle',
    index=1,
    containing_service=None,
    input_type=_AUTHORIZE,
    output_type=_ANSWER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='user_finish',
    full_name='Authentication.user_finish',
    index=2,
    containing_service=None,
    input_type=_FINISH,
    output_type=_ANSWER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_AUTHENTICATION)

DESCRIPTOR.services_by_name['Authentication'] = _AUTHENTICATION

# @@protoc_insertion_point(module_scope)
