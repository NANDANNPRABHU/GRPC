import grpc
from concurrent import futures
import network_pb2
import network_pb2_grpc
import uuid

class NetworkServicer(network_pb2_grpc.NetworkServicer):
    def __init__(self):
        self.clients = {}

    def Join(self, request, context):
        client_id = str(uuid.uuid4())
        self.clients[client_id] = request.client_address
        print(f"Client {client_id} joined with address {request.client_address}")
        return network_pb2.JoinResponse(client_id=client_id)

    def SendMessage(self, request, context):
        receiver_address = self.clients.get(request.receiver_id)
        if receiver_address:
            # In a real-world scenario, you would send this message to the receiver using gRPC
            print(f"Message from {request.sender_id} to {request.receiver_id}: {request.text}")
        return network_pb2.Empty()

    def ReceiveMessages(self, request_iterator, context):
        for message in request_iterator:
            print(f"Received message from {message.sender_id} to {message.receiver_id}: {message.text}")
        return network_pb2.Empty()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    network_pb2_grpc.add_NetworkServicer_to_server(NetworkServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server started on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
