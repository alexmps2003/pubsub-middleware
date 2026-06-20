import socket
import sys
import threading


clients = []
clients_lock = threading.Lock()


def broadcast_to_subscribers(message, sender_socket):
    with clients_lock:
        for client in clients:
            if client["role"] == "SUBSCRIBER" and client["socket"] != sender_socket:
                try:
                    client["socket"].sendall(message.encode("utf-8"))
                except:
                    pass


def handle_client(client_socket, client_address):
    try:
        role_data = client_socket.recv(1024)
        role = role_data.decode("utf-8").strip().upper()

        if role not in ["PUBLISHER", "SUBSCRIBER"]:
            client_socket.sendall("Invalid role. Use PUBLISHER or SUBSCRIBER.".encode("utf-8"))
            client_socket.close()
            return

        with clients_lock:
            clients.append({
                "socket": client_socket,
                "address": client_address,
                "role": role
            })

        print(f"{role} connected from {client_address}")

        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode("utf-8")

            if message.lower() == "terminate":
                print(f"{role} from {client_address} disconnected using terminate.")
                break

            print(f"Message from {role} {client_address}: {message}")

            if role == "PUBLISHER":
                formatted_message = f"[Publisher {client_address}] {message}"
                broadcast_to_subscribers(formatted_message, client_socket)

    except ConnectionResetError:
        print(f"Connection lost from {client_address}")

    finally:
        with clients_lock:
            clients[:] = [client for client in clients if client["socket"] != client_socket]

        client_socket.close()
        print(f"Cleaned up connection from {client_address}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 server.py <PORT>")
        return

    port = int(sys.argv[1])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen()

    print("TASK 2 PUB/SUB SERVER STARTED")
    print(f"Listening on port {port}")
    print("Waiting for publishers and subscribers...")

    while True:
        client_socket, client_address = server_socket.accept()

        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )

        client_thread.start()


if __name__ == "__main__":
    main()