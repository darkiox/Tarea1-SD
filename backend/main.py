from re import search
import grpc
from concurrent import futures
import proto_response_pb2 as proto_pb2
import proto_response_pb2_grpc as proto_pb2_grpc
from time import sleep
import psycopg2

class SearchService(proto_pb2_grpc.SearchServicer):
    def __init__(self, *args, **kwargs):
        pass
    def GetServerResponse(self, request, context):
        response=[]
        result = f'"{request.message}"'
        query = "SELECT * FROM urls WHERE keywords LIKE '%" + request.message + "%';"
        cursor.execute(query)
        queryres = cursor.fetchall()
        if len(queryres) == 0:
            result = dict()
            result['error'] = "404 not found."
            response.append(result)
            return proto_pb2.SearchResults(response=response)
        for entry in queryres:
            result = dict()
            # 0 = id
            # 1 = title
            # 2 = description
            # 3 = keywords
            # 4 = url
            result['title'] = entry[1]
            result['description'] = entry[2]
            result['url'] = entry[4]
            response.append(result)
        return proto_pb2.SearchResults(response=response)

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proto_pb2_grpc.add_SearchServicer_to_server(SearchService(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
    
sleep(15)
dbconnect = psycopg2.connect("dbname=tarea user=postgres password=postgrespw host=db-tarea")
cursor = dbconnect.cursor()
server()