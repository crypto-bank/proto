# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exchange/exchange.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='exchange/exchange.proto',
  package='exchange',
  syntax='proto3',
  serialized_pb=_b('\n\x17\x65xchange/exchange.proto\x12\x08\x65xchange\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto*H\n\x08\x45xchange\x12\x1a\n\x08POLONIEX\x10\x00\x1a\x0c\x8a\x9d \x08Poloniex\x12\x1a\n\x08\x42ITFINEX\x10\x01\x1a\x0c\x8a\x9d \x08\x42itfinex\x1a\x04\x88\xa3\x1e\x00\x42\x0c\xd0\xe2\x1e\x01\xc8\xe2\x1e\x01\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EXCHANGE = _descriptor.EnumDescriptor(
  name='Exchange',
  full_name='exchange.Exchange',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='POLONIEX', index=0, number=0,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \010Poloniex')),
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BITFINEX', index=1, number=1,
      options=_descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \010Bitfinex')),
      type=None),
  ],
  containing_type=None,
  options=_descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000')),
  serialized_start=84,
  serialized_end=156,
)
_sym_db.RegisterEnumDescriptor(_EXCHANGE)

Exchange = enum_type_wrapper.EnumTypeWrapper(_EXCHANGE)
POLONIEX = 0
BITFINEX = 1


DESCRIPTOR.enum_types_by_name['Exchange'] = _EXCHANGE


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\320\342\036\001\310\342\036\001\250\342\036\001'))
_EXCHANGE.has_options = True
_EXCHANGE._options = _descriptor._ParseOptions(descriptor_pb2.EnumOptions(), _b('\210\243\036\000'))
_EXCHANGE.values_by_name["POLONIEX"].has_options = True
_EXCHANGE.values_by_name["POLONIEX"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \010Poloniex'))
_EXCHANGE.values_by_name["BITFINEX"].has_options = True
_EXCHANGE.values_by_name["BITFINEX"]._options = _descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), _b('\212\235 \010Bitfinex'))
# @@protoc_insertion_point(module_scope)