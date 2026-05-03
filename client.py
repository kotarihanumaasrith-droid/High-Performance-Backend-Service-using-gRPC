import grpc
import service_pb2
import service_pb2_grpc


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.UserServiceStub(channel)

    response = stub.GetUser(service_pb2.UserRequest(user_id=1))

    print("User ID:", response.user_id)
    print("Name:", response.name)
    print("Email:", response.email)


if __name__ == '__main__':
    run()
