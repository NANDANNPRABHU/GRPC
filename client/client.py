import grpc
import network_pb2
import network_pb2_grpc

class Client:
    def __init__(self, server_address):
        self.server_address = server_address
        self.channel = grpc.insecure_channel(server_address)
        self.stub = network_pb2_grpc.NetworkStub(self.channel)
        self.client_id = None

    def join_network(self):
        response = self.stub.Join(network_pb2.JoinRequest(client_address=self.server_address))
        self.client_id = response.client_id
        print(f"Joined network with client ID: {self.client_id}")

    def send_message(self, receiver_id, text):
        message = network_pb2.Message(sender_id=self.client_id, receiver_id=receiver_id, text=text)
        self.stub.SendMessage(message)

    def receive_messages(self):
        for message in self.stub.ReceiveMessages(network_pb2.Empty()):
            print(f"Message from {message.sender_id}: {message.text}")

if __name__ == "__main__":
    client = Client('localhost:50051')
    client.join_network()
    
    # Example usage: send and receive messages
    client.send_message("receiver_id_placeholder", "Hello, World!")
    client.receive_messages()
