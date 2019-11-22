import numpy as np
import keyboard
from time import sleep, time
from json import dumps
from kafka import KafkaConsumer, KafkaProducer

BROKER_ADDRESS = 'localhost:9092'

class Vehicle:
    def __init__(self, vehicle_id, x_initial, y_initial, battery):
        self.location = (x_initial, y_initial)
        self.producer = KafkaProducer(bootstrap_servers=[BROKER_ADDRESS])
        self.vehicle_id = vehicle_id
        self.battery = battery

    def send_location(self, x=None, y=None):
        self.location = (np.random.normal(float(self.location[0]), 100, 1)[0], np.random.normal(float(self.location[1]), 100, 1)[0])
        self.producer.send('locations', key=bytes(str(self.vehicle_id), encoding='utf-8'), value=bytes(str([(self.location), self.battery]), encoding='utf-8'))
    
    def check_authorization(self):
        consumer = KafkaConsumer('authorizations', bootstrap_servers=[BROKER_ADDRESS],
                                auto_offset_reset='latest', enable_auto_commit=True,
                                consumer_timeout_ms=10000)
        begin_time = time()
        answer = False
        for message in consumer:
            if (message.key.decode('utf-8') == str(self.vehicle_id)):
                answer = message.value.decode('utf-8')
                break
        consumer.close()
        return answer

    def check_finish(self):
        consumer = KafkaConsumer('finish', bootstrap_servers=[BROKER_ADDRESS],
                                auto_offset_reset='latest', enable_auto_commit=True)
        for message in consumer:
            if (message.key.decode('utf-8') == str(self.vehicle_id)):
                break
        consumer.close()
    def start_vehicle(self):
        print("Starting vehicle. Id: {}".format(self.vehicle_id))
        last_time = time()
        while True:
            if keyboard.is_pressed('q'):
                aut = self.check_authorization()
                print(aut)
                if(aut=='True'):
                    self.check_finish()
                print('get to finish')
            if(time()-last_time>5):
                self.send_location()
                last_time = time()

x = Vehicle(3, '100', '100', 30)
x.start_vehicle()
