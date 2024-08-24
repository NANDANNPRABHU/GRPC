import os
import grpc_tools.protoc

PROTO_FILE = "network.proto"

def generate_grpc_code():
    grpc_tools.protoc.main([
        'grpc_tools.protoc',
        '--proto_path=.',
        '--python_out=../generated',
        '--grpc_python_out=../generated',
        PROTO_FILE
    ])

if __name__ == '__main__':
    generate_grpc_code()
