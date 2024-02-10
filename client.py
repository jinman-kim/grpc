import grpc
import message_pb2
import message_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = message_pb2_grpc.MessageServiceStub(channel)
        response = stub.SendMessage(message_pb2.MessageRequest(name='World'))
        print(f"Server response: {response.greeting}")

if __name__ == '__main__':
    run()

