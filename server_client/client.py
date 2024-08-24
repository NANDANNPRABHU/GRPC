import grpc
import persistent_streaming_pb2
import persistent_streaming_pb2_grpc
import time

def generate_messages(client_id):
    # This function generates a stream of messages to send to the server
    while True:
        message = input(f"Enter message to send to server as {client_id}: ")
        yield persistent_streaming_pb2.ClientMessage(user=client_id, message=message)
        time.sleep(1)  # Wait for a second before sending the next message

def run(client_id):
    with grpc.insecure_channel('172.17.0.2:50051') as channel:  # Replace with server's IP
        stub = persistent_streaming_pb2_grpc.PersistentChatServiceStub(channel)
        
        # Register the client
        registration_response = stub.RegisterClient(persistent_streaming_pb2.ClientMessage(user=client_id, message=""))
        print(registration_response.message)
        
        # Start chatting
        responses = stub.Chat(generate_messages(client_id))
        for response in responses:
            print(f"Received message from {response.from_user}: {response.message}")

if __name__ == '__main__':
    client_id = input("Enter your client ID: ")
    run(client_id)
