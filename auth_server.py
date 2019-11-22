import grpc
from concurrent import futures
import time
from kafka import KafkaProducer
import authentication_pb2
import authentication_pb2_grpc
import psycopg2

BROKER_ADDRESS = 'localhost:9092'


class Listener(authentication_pb2_grpc.AuthenticationServicer):
    def __init__(self, db):
        self.db = db
        self.cur = self.db.cursor()
        self.producer = KafkaProducer(bootstrap_servers=[BROKER_ADDRESS])
    def makelogin(self, request, context):
        '''este metodo realiza a autenticação do login'''
        response = authentication_pb2.Answer()
        self.cur.execute("select * from usuarios where email='{}'".format(request.name))
        recset = self.cur.fetchone()
        try:
            if(recset[3] == request.password):
                response.is_auth = True
            else:
                response.is_auth = False
        except:
            response.is_auth = False

        return response

    def user_finish(self,request, context):
        response = authentication_pb2.Answer()
        self.cur.execute("select * from usuarios where email='{}'".format(request.user_id))
        recset = self.cur.fetchone()
        user = recset[0]
        self.cur.execute("insert into viagens (codigo, distancia, ped_usuario, ped_veiculo, custo) values ('{}', '{}', '{}', '{}', '{}')".format(15, request.tempo, user, request.vehicle_id, '100'))
        self.db.commit()
        self.producer.send('finish', key=bytes(str(request.vehicle_id), encoding='utf-8'), value=bytes('True', encoding='utf-8'))
        response = authentication_pb2.Answer()
        response.is_auth = True
        return response
    def authorize_vehicle(self, request, context):
        '''este metodo recebe um objeto Authorize e retorna TRUE se
        a carteira e bateria estão corretos
        '''
        response = authentication_pb2.Answer()
        self.cur.execute("select * from veiculos where codigo='{}'".format(request.vehicle_id))
        recset = self.cur.fetchone()
        battery = recset[2]
        if(battery<=5):
            response.is_auth = False
            return response
        self.cur.execute("select * from usuarios where email='{}'".format(request.user_id))
        recset = self.cur.fetchone()
        carteira = recset[5]
        if(carteira>0):
            response.is_auth = True
        else:
            response.is_auth = False
        
        self.producer.send('authorizations', key=bytes(str(request.vehicle_id), encoding='utf-8'), 
                    value=bytes(str(response.is_auth), encoding='utf-8'))
        return response

def start_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    con = psycopg2.connect(host='localhost', database='mobility_volt', user='postgres', password='ec8z21')
    #db = con.cursor()
    authentication_pb2_grpc.add_AuthenticationServicer_to_server(Listener(con), server)

    print('Starting server. Listening on port 5001')
    server.add_insecure_port('[::]:5001')
    server.start()
    try:
      while True:
          time.sleep(86400)
    except KeyboardInterrupt:
        con.close()
        server.stop(0)

if __name__=='__main__':
    start_server()