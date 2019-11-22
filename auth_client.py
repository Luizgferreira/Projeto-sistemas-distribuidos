import grpc
import socket
import authentication_pb2
import authentication_pb2_grpc

def loginrequest(name, password, server_address):
    channel = grpc.insecure_channel(server_address+':5001')
    stub = authentication_pb2_grpc.AuthenticationStub(channel)
    login_request = authentication_pb2.Login(name=name,password=password)
    response = stub.makelogin(login_request)
    return response.is_auth

def authrequest(user_id, vehicle_id, server_address):
    channel = grpc.insecure_channel(server_address+':5001')
    stub = authentication_pb2_grpc.AuthenticationStub(channel)
    auth_request = authentication_pb2.Authorize(user_id=user_id, vehicle_id=vehicle_id)
    response = stub.authorize_vehicle(auth_request)
    return response.is_auth


print(loginrequest("erikson@usp.br", '321234', socket.gethostname()))
#print(authrequest(10, 10, socket.gethostname()))
