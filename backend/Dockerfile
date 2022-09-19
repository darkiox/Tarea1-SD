FROM python:3.9-bullseye
WORKDIR /backend
COPY requirements.txt /backend
COPY . .
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc -I ./ --python_out=. --grpc_python_out=. ./proto_response.proto
EXPOSE 3000
CMD ["python", "main.py"]
