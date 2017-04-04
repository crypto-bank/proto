# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orderbook/orderbook.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from github.com.gogo.protobuf.gogoproto import gogo_pb2 as github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2
from github.com.crypto_bank.proto.order import order_pb2 as github_dot_com_dot_crypto__bank_dot_proto_dot_order_dot_order__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orderbook/orderbook.proto',
  package='orderbook',
  syntax='proto3',
  serialized_pb=_b('\n\x19orderbook/orderbook.proto\x12\torderbook\x1a-github.com/gogo/protobuf/gogoproto/gogo.proto\x1a.github.com/crypto-bank/proto/order/order.proto\"N\n\x05\x45vent\x12\x1d\n\x05order\x18\x01 \x01(\x0b\x32\x0c.order.OrderH\x00\x12\x1d\n\x05trade\x18\x02 \x01(\x0b\x32\x0c.order.TradeH\x00\x42\x07\n\x05\x65vent2\x0b\n\tOrderBookB\x17Z\torderbook\xd0\xe2\x1e\x01\xc8\xe2\x1e\x01\xa8\xe2\x1e\x01\x62\x06proto3')
  ,
  dependencies=[github_dot_com_dot_gogo_dot_protobuf_dot_gogoproto_dot_gogo__pb2.DESCRIPTOR,github_dot_com_dot_crypto__bank_dot_proto_dot_order_dot_order__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='orderbook.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order', full_name='orderbook.Event.order', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trade', full_name='orderbook.Event.trade', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='event', full_name='orderbook.Event.event',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=135,
  serialized_end=213,
)

_EVENT.fields_by_name['order'].message_type = github_dot_com_dot_crypto__bank_dot_proto_dot_order_dot_order__pb2._ORDER
_EVENT.fields_by_name['trade'].message_type = github_dot_com_dot_crypto__bank_dot_proto_dot_order_dot_order__pb2._TRADE
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['order'])
_EVENT.fields_by_name['order'].containing_oneof = _EVENT.oneofs_by_name['event']
_EVENT.oneofs_by_name['event'].fields.append(
  _EVENT.fields_by_name['trade'])
_EVENT.fields_by_name['trade'].containing_oneof = _EVENT.oneofs_by_name['event']
DESCRIPTOR.message_types_by_name['Event'] = _EVENT

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'orderbook.orderbook_pb2'
  # @@protoc_insertion_point(class_scope:orderbook.Event)
  ))
_sym_db.RegisterMessage(Event)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\torderbook\320\342\036\001\310\342\036\001\250\342\036\001'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class OrderBookStub(object):
    """Orders - Streams order book updates.
    rpc Orders(OrdersRequest) returns (stream OrderBookUpdate) {};
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """


  class OrderBookServicer(object):
    """Orders - Streams order book updates.
    rpc Orders(OrdersRequest) returns (stream OrderBookUpdate) {};
    """


  def add_OrderBookServicer_to_server(servicer, server):
    rpc_method_handlers = {
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'orderbook.OrderBook', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaOrderBookServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Orders - Streams order book updates.
    rpc Orders(OrdersRequest) returns (stream OrderBookUpdate) {};
    """


  class BetaOrderBookStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """Orders - Streams order book updates.
    rpc Orders(OrdersRequest) returns (stream OrderBookUpdate) {};
    """


  def beta_create_OrderBook_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
    }
    response_serializers = {
    }
    method_implementations = {
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_OrderBook_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
    }
    response_deserializers = {
    }
    cardinalities = {
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'orderbook.OrderBook', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)