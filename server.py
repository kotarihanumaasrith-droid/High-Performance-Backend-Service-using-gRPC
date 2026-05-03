import grpc
from concurrent import futures
import time

import service_pb2
import service_pb2_grpc

# Dummy database
USERS_DB = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"},
}

class UserService(service_pb2_grpc.UserServiceServicer):

    def GetUser(self, request, context):
        user = USERS_DB.get(request.user_id)

        if not user:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User not found")
            return service_pb2.UserResponse()

        return service_pb2.UserResponse(
            user_id=request.user_id,
            name=user["name"],
            email=user["email"]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051...")

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
