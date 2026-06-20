import socket
import sys
import threading


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                break

            print(f"\n{data.decode('utf-8')}")
            print("> ", end="", flush=True)

        except:
            break


def main():
    if len(sys.argv) != 5:
        print("Usage: python3 client.py <SERVER_IP> <PORT> <ROLE> <TOPIC>")
        print("Example: python3 client.py 127.0.0.1 8000 PUBLISHER SPORTS")
        return

    server_ip = sys.argv[1]
    port = int(sys.argv[2])
    role = sys.argv[3].upper()
    topic = sys.argv[4].upper()

    if role not in ["PUBLISHER", "SUBSCRIBER"]:
        print("Invalid role. Use PUBLISHER or SUBSCRIBER.")
        return

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, port))

    client_socket.sendall(f"{role}:{topic}".encode("utf-8"))

    print("TASK 2 CLIENT STARTED")
    print(f"Connected to server at {server_ip}:{port}")
    print(f"Role: {role}")
    print(f"Topic: {topic}")
    print("Type messages and press Enter.")
    print("Type 'terminate' to disconnect.")

    if role == "SUBSCRIBER":
        receiver_thread = threading.Thread(
            target=receive_messages,
            args=(client_socket,),
            daemon=True
        )
        receiver_thread.start()

    while True:
        message = input("> ")

        client_socket.sendall(message.encode("utf-8"))

        if message.lower() == "terminate":
            break

    client_socket.close()
    print("Client terminated.")


if __name__ == "__main__":
    main()