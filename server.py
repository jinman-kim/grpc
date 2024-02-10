from concurrent import futures
import grpc
import message_pb2
import message_pb2_grpc

class MessageServiceServicer(message_pb2_grpc.MessageServiceServicer):
    def SendMessage(self, request, context):
        response = message_pb2.MessageResponse()
        response.greeting = f"Hello, {request.name}!"
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    message_pb2_grpc.add_MessageServiceServicer_to_server(MessageServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

