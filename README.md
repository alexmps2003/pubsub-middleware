# Publish/Subscribe Middleware

A simple Publish/Subscribe middleware system implemented in Python using TCP sockets.

## Features

- Task 1: Client-Server communication
- Task 2: Publisher/Subscriber communication
- Task 3: Topic-based Publish/Subscribe

## Requirements

- Python 3

## Running the Server

```bash
python3 server.py 8000
```

## Running Clients

Publisher

```bash
python3 client.py 127.0.0.1 8000 PUBLISHER SPORTS
```

Subscriber

```bash
python3 client.py 127.0.0.1 8000 SUBSCRIBER SPORTS
```

## Docker

Build

```bash
docker build -t pubsub-middleware .
```

Run

```bash
docker run -p 8000:8000 pubsub-middleware
```