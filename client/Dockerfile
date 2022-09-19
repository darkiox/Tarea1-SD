FROM python:3.9-bullseye
WORKDIR /client
COPY proto_response.proto ./
COPY requirements.txt /client
RUN pip3 install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./proto_response.proto
ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1
EXPOSE 9000
COPY . .
CMD ["flask", "run"]