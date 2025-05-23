# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import persistent_streaming_pb2 as persistent__streaming__pb2


class PersistentChatServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterClient = channel.unary_unary(
                '/PersistentChatService/RegisterClient',
                request_serializer=persistent__streaming__pb2.ClientMessage.SerializeToString,
                response_deserializer=persistent__streaming__pb2.ServerMessage.FromString,
                )
        self.Chat = channel.stream_stream(
                '/PersistentChatService/Chat',
                request_serializer=persistent__streaming__pb2.ClientMessage.SerializeToString,
                response_deserializer=persistent__streaming__pb2.ServerMessage.FromString,
                )


class PersistentChatServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RegisterClient(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Chat(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PersistentChatServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterClient,
                    request_deserializer=persistent__streaming__pb2.ClientMessage.FromString,
                    response_serializer=persistent__streaming__pb2.ServerMessage.SerializeToString,
            ),
            'Chat': grpc.stream_stream_rpc_method_handler(
                    servicer.Chat,
                    request_deserializer=persistent__streaming__pb2.ClientMessage.FromString,
                    response_serializer=persistent__streaming__pb2.ServerMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PersistentChatService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PersistentChatService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PersistentChatService/RegisterClient',
            persistent__streaming__pb2.ClientMessage.SerializeToString,
            persistent__streaming__pb2.ServerMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Chat(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/PersistentChatService/Chat',
            persistent__streaming__pb2.ClientMessage.SerializeToString,
            persistent__streaming__pb2.ServerMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
