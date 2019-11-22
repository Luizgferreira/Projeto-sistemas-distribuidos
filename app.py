import numpy as np
import keyboard
from time import sleep, time
from json import dumps
from kafka import KafkaConsumer, KafkaProducer
import grpc
import socket
import authentication_pb2
import authentication_pb2_grpc


BROKER_ADDRESS = 'localhost:9092'
class App:
	def __init__(self, server_address):
		channel = grpc.insecure_channel(server_address+':5001')
		self.stub = authentication_pb2_grpc.AuthenticationStub(channel)
	def loginrequest(self, password):
	    #channel = grpc.insecure_channel(server_address+':5001')
	    #stub = authentication_pb2_grpc.AuthenticationStub(channel)
	    login_request = authentication_pb2.Login(name=self.user,password=password)
	    response = self.stub.makelogin(login_request)
	    return response.is_auth

	def authrequest(self, vehicle_id):
	    #channel = grpc.insecure_channel(server_address+':5001')
	    #stub = authentication_pb2_grpc.AuthenticationStub(channel)
	    auth_request = authentication_pb2.Authorize(user_id=self.user, vehicle_id=vehicle_id)
	    response = self.stub.authorize_vehicle(auth_request)
	    return response.is_auth


	def find_locations(self):
		consumer = KafkaConsumer('locations', bootstrap_servers=[BROKER_ADDRESS],
                            		auto_offset_reset='earliest', enable_auto_commit=True, 
                            		consumer_timeout_ms=1000)

		self.vehicles = {}
		for message in consumer:
			self.vehicles[message.key.decode('utf-8')] = message.value.decode('utf-8')
		consumer.close()
		return self.vehicles

	def start_app(self):
		print("Starting app...")
		self.user = input('Email: ')
		password = input('Password: ')
		res = self.loginrequest(password)
		print("Answer to makeLogin: {}".format(res))
		print(self.find_locations())
		vehicle = input("Which id: ")
		auth = self.authrequest(int(vehicle))
		print('Answer to authrequest: {}'.format(auth))
		sleep(15)
		auth_request = authentication_pb2.Finish(user_id=self.user, vehicle_id=int(vehicle), tempo=100)
		response = self.stub.user_finish(auth_request)



x = App(socket.gethostname())
x.start_app()