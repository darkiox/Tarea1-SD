import json
from flask import Flask, request, render_template, app, jsonify
import proto_response_pb2 as pb2
import proto_response_pb2_grpc as pb2_grpc
import redis
import grpc
import time
from google.protobuf.json_format import MessageToJson

# Definir redis master
redis_master = redis.Redis(host="redis-1", port=6379, db=0)
redis_master.flushall()
app = Flask(__name__)

class Client(object):
    def __init__(self):
        self.host = "backend-tarea"
        self.port = "50051"
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.port))
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_url(self, message):
        message = pb2.Message(message = message)
        print(f'{message}')
        stub = self.stub.GetServerResponse(message)
        return stub

@app.route('/', methods = ['GET'])
def frontend():
    return render_template('frontend.html' , searchresults = "No se ha buscado nada aún." , src = "")

@app.route('/front', methods = ['GET'])
def frontquery():
    client = Client()
    search = request.args['search']
    if redis_master.get(search) != None:
        data = redis_master.get(search).decode("utf-8")
        return render_template('frontend.html', searchresults = data, src = "Source: Redis")
    else:
        data = client.get_url(message=search)
        data = MessageToJson(data)
        redis_master.set(search,data)
        return render_template('frontend.html', searchresults = data, src = "Source: postgresql")

@app.route('/search', methods = ['GET'])
def search():
    client = Client()
    search = request.args['q']
    print('Se ha ingresado:', request.args['q'], flush=True)
    if redis_master.get(search) != None:
        data = redis_master.get(search).decode("utf-8")
        return render_template('index.html', searchresults = data, src = "Redis")
    else:
        data = client.get_url(message=search)
        data = MessageToJson(data)
        redis_master.set(search,data)
        return render_template('index.html', searchresults = data, src = "postgresql")


# Esperar al backend
time.sleep(20)