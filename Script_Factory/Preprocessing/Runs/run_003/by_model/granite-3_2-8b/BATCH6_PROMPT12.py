# BATCH6_PROMPT12_{model_name}.py

import socket
import random

def generate_nonsensical_data(length=10):
    """Generates a random string of characters."""
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
    return ''.join(random.choice(letters) for _ in range(length))

def handle_client(client_socket):
    """Handles a single client connection."""
    try:
        print(f"New connection from {client_socket.getpeername()}")

        # 40% chance to close the connection immediately
        if random.random() > 0.4:
            print("Closing connection due to flakiness.")
            client_socket.close()
            return

        # 60% chance to send nonsensical data
        nonsense = generate_nonsensical_data(10)
        client_socket.sendall(nonsense.encode())
        print(f"Sent nonsensical data: {nonsense}")

    except Exception as e:
        print(f"Error handling client: {e}")
    finally:
        client_socket.close()

def main():
    """Sets up the socket server."""
    HOST = '0.0.0.0'  # Listen on all available interfaces
    PORT = 65432      # Port to listen on

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Unreliable API Simulator listening on {HOST}:{PORT}")

        while True:
            client_socket, addr = s.accept()
            print(f"Accepted connection from {addr}")
            handle_client(client_socket)

if __name__ == "__main__":
    main()