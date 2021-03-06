# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spacy_grpc/spacy.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spacy_grpc/spacy.proto',
  package='spaCy',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16spacy_grpc/spacy.proto\x12\x05spaCy\"\x1b\n\x07Request\x12\x10\n\x08sentence\x18\x01 \x01(\t\"`\n\x05Token\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03tag\x18\x02 \x01(\t\x12\r\n\x05lemma\x18\x03 \x01(\t\x12\x0e\n\x06\x65ntity\x18\x04 \x01(\t\x12\r\n\x05index\x18\x05 \x01(\r\x12\x0e\n\x06length\x18\x06 \x01(\r\"%\n\x05Reply\x12\x1c\n\x06tokens\x18\x01 \x03(\x0b\x32\x0c.spaCy.Token2U\n\x05SpaCy\x12%\n\x03Tag\x12\x0e.spaCy.Request\x1a\x0c.spaCy.Reply\"\x00\x12%\n\x03NER\x12\x0e.spaCy.Request\x1a\x0c.spaCy.Reply\"\x00\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='spaCy.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sentence', full_name='spaCy.Request.sentence', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=33,
  serialized_end=60,
)


_TOKEN = _descriptor.Descriptor(
  name='Token',
  full_name='spaCy.Token',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='spaCy.Token.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag', full_name='spaCy.Token.tag', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lemma', full_name='spaCy.Token.lemma', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entity', full_name='spaCy.Token.entity', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index', full_name='spaCy.Token.index', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='spaCy.Token.length', index=5,
      number=6, type=13, cpp_type=3, label=1,
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
  serialized_start=62,
  serialized_end=158,
)


_REPLY = _descriptor.Descriptor(
  name='Reply',
  full_name='spaCy.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tokens', full_name='spaCy.Reply.tokens', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=160,
  serialized_end=197,
)

_REPLY.fields_by_name['tokens'].message_type = _TOKEN
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Token'] = _TOKEN
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'spacy_grpc.spacy_pb2'
  # @@protoc_insertion_point(class_scope:spaCy.Request)
  })
_sym_db.RegisterMessage(Request)

Token = _reflection.GeneratedProtocolMessageType('Token', (_message.Message,), {
  'DESCRIPTOR' : _TOKEN,
  '__module__' : 'spacy_grpc.spacy_pb2'
  # @@protoc_insertion_point(class_scope:spaCy.Token)
  })
_sym_db.RegisterMessage(Token)

Reply = _reflection.GeneratedProtocolMessageType('Reply', (_message.Message,), {
  'DESCRIPTOR' : _REPLY,
  '__module__' : 'spacy_grpc.spacy_pb2'
  # @@protoc_insertion_point(class_scope:spaCy.Reply)
  })
_sym_db.RegisterMessage(Reply)



_SPACY = _descriptor.ServiceDescriptor(
  name='SpaCy',
  full_name='spaCy.SpaCy',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=199,
  serialized_end=284,
  methods=[
  _descriptor.MethodDescriptor(
    name='Tag',
    full_name='spaCy.SpaCy.Tag',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NER',
    full_name='spaCy.SpaCy.NER',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_REPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SPACY)

DESCRIPTOR.services_by_name['SpaCy'] = _SPACY

# @@protoc_insertion_point(module_scope)
