# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import products_pb2 as products__pb2


class ProductsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddSellerProduct = channel.unary_unary(
                '/products.Products/AddSellerProduct',
                request_serializer=products__pb2.ProductItemMessage.SerializeToString,
                response_deserializer=products__pb2.generalResponse.FromString,
                )
        self.EditSellerProduct = channel.unary_unary(
                '/products.Products/EditSellerProduct',
                request_serializer=products__pb2.ProductItemMessage.SerializeToString,
                response_deserializer=products__pb2.generalResponse.FromString,
                )
        self.GetSellerProducts = channel.unary_unary(
                '/products.Products/GetSellerProducts',
                request_serializer=products__pb2.ProductItemMessage.SerializeToString,
                response_deserializer=products__pb2.generalResponse.FromString,
                )
        self.RemoveSellerProduct = channel.unary_unary(
                '/products.Products/RemoveSellerProduct',
                request_serializer=products__pb2.ProductItemMessage.SerializeToString,
                response_deserializer=products__pb2.generalResponse.FromString,
                )
        self.GetSellerRatings = channel.unary_unary(
                '/products.Products/GetSellerRatings',
                request_serializer=products__pb2.ProductItemMessage.SerializeToString,
                response_deserializer=products__pb2.generalResponse.FromString,
                )


class ProductsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddSellerProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EditSellerProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSellerProducts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSellerProduct(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSellerRatings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProductsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddSellerProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSellerProduct,
                    request_deserializer=products__pb2.ProductItemMessage.FromString,
                    response_serializer=products__pb2.generalResponse.SerializeToString,
            ),
            'EditSellerProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.EditSellerProduct,
                    request_deserializer=products__pb2.ProductItemMessage.FromString,
                    response_serializer=products__pb2.generalResponse.SerializeToString,
            ),
            'GetSellerProducts': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSellerProducts,
                    request_deserializer=products__pb2.ProductItemMessage.FromString,
                    response_serializer=products__pb2.generalResponse.SerializeToString,
            ),
            'RemoveSellerProduct': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSellerProduct,
                    request_deserializer=products__pb2.ProductItemMessage.FromString,
                    response_serializer=products__pb2.generalResponse.SerializeToString,
            ),
            'GetSellerRatings': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSellerRatings,
                    request_deserializer=products__pb2.ProductItemMessage.FromString,
                    response_serializer=products__pb2.generalResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'products.Products', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Products(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddSellerProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/products.Products/AddSellerProduct',
            products__pb2.ProductItemMessage.SerializeToString,
            products__pb2.generalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def EditSellerProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/products.Products/EditSellerProduct',
            products__pb2.ProductItemMessage.SerializeToString,
            products__pb2.generalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSellerProducts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/products.Products/GetSellerProducts',
            products__pb2.ProductItemMessage.SerializeToString,
            products__pb2.generalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveSellerProduct(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/products.Products/RemoveSellerProduct',
            products__pb2.ProductItemMessage.SerializeToString,
            products__pb2.generalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSellerRatings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/products.Products/GetSellerRatings',
            products__pb2.ProductItemMessage.SerializeToString,
            products__pb2.generalResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
