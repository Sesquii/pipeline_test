```python
import socket
import random

def main():
    # Create and bind a TCP socket to listen on port 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    
    print("Server started. Waiting for connections...")
    
    while True:
        # Accept a new connection from client
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        # With 40% chance, close the connection immediately
        if random.random() < 0.4:
            print("Closing connection immediately.")
            client_socket.close()
            continue
        
        # Generate random string of nonsensical data (10 characters)
        data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=10))
        client_socket.sendall(data.encode())
        
        # Close the socket after sending data
        client_socket.close()

if __name__ == "__main__":
    main()