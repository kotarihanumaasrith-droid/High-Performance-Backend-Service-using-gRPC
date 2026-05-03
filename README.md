# High-Performance Backend Service using gRPC

## Overview
Python-based backend using gRPC for efficient inter-service communication.

## Features
- HTTP/2 communication
- Protocol Buffers (Protobuf)
- Low latency vs REST
- Scalable service architecture

## Setup

### 1. Install dependencies
pip install -r requirements.txt

### 2. Generate gRPC files
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service.proto

### 3. Run server
python server.py

### 4. Run client
python client.py

## gRPC vs REST
- gRPC → binary (faster)
- REST → JSON (human-readable)
- gRPC → HTTP/2 multiplexing
- REST → HTTP/1.1 mostly

## Notes
- Default port: 50051
- Replace dummy DB with real database in production
