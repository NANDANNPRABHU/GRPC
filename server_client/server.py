import grpc
from concurrent import futures
import time
import threading
import persistent_streaming_pb2
import persistent_streaming_pb2_grpc

# Global dictionary to store connected clients with their IDs
connected_clients = {}

class PersistentChatService(persistent_streaming_pb2_grpc.PersistentChatServiceServicer):
    def RegisterClient(self, request, context):
        client_id = request.user
        client_address = context.peer()  # Get client's address
        connected_clients[client_id] = client_address
        print(f"Client {client_id} connected from {client_address}")
        return persistent_streaming_pb2.ServerMessage(
            message=f"Client {client_id} registered.",
            from_user="Server"
        )
    
    def Chat(self, request_iterator, context):
        for client_message in request_iterator:
            print(f"Received message from {client_message.user}: {client_message.message}")
            # Respond back to the client
            yield persistent_streaming_pb2.ServerMessage(
                message=f"Hello {client_message.user}, your message was received.",
                from_user="Server"
            )

def print_connected_clients():
    while True:
        time.sleep(5)  # Wait for 5 seconds
        print("\nConnected clients:")
        for client_id, client_address in connected_clients.items():
            print(f" - {client_id}: {client_address}")
        print("-" * 20)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    persistent_streaming_pb2_grpc.add_PersistentChatServiceServicer_to_server(PersistentChatService(), server)
    server.add_insecure_port('0.0.0.0:50051')  # Bind to all available network interfaces
    server.start()
    print("Server started on port 50051.")
    
    # Start the thread to print connected clients
    # threading.Thread(target=print_connected_clients, daemon=True).start()

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
