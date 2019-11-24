from time import sleep, time
from json import dumps
import grpc
import numpy as np
import socket
import authentication_pb2
import authentication_pb2_grpc
from kafka import KafkaProducer


n = 100
BROKER_ADDRESS = 'localhost:9092'
antes = time()
while True:
	vehicle_id = np.random.randint(0, n)
	producer = KafkaProducer(bootstrap_servers=[BROKER_ADDRESS])
	producer.send('authorizations', key=bytes(str(vehicle_id), encoding='utf-8'), 
	                  value=bytes(str(True), encoding='utf-8'))
	#sleep(1/n)
	depois = time()
	print(antes-depois)
	antes = depois


'''
n = 1000000
while True:
	channel = grpc.insecure_channel('127.0.0.1:5001')
	stub = authentication_pb2_grpc.AuthenticationStub(channel)
	user = 'erikson@usp.br'
	password = '321234'
	login_request = authentication_pb2.Login(name=user,password=password)
	response = stub.makelogin(login_request)
	sleep(1/n)
'''