# Import necessary libraries
import socket
import random

def unreliable_api_simulator(host='0.0.0.0', port=12345):
    """
    Simulates an unreliable API using a simple socket server.
    
    The server accepts connections and, with a 40% chance, closes the connection immediately without sending any data.
    With a 60% chance, it sends back a random string of nonsensical data.
    """
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Server listening on {host}:{port}")
    
    try:
        while True:
            # Accept a connection
            client_socket, addr = server_socket.accept()
            print(f"Connection from {addr}")
            
            # Randomly decide whether to close the connection or send data
            if random.choice([True, False, False]):  # 40% chance
                print("Closing connection without sending data")
                client_socket.close()
            else:  # 60% chance
                # Generate a random string of nonsensical data
                data = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10))
                print(f"Sending data: {data}")
                
                # Send the data to the client
                client_socket.sendall(data.encode())
                
                # Close the connection after sending data
                client_socket.close()
    except KeyboardInterrupt:
        print("Server shutting down")
    finally:
        server_socket.close()

# Entry point of the program
if __name__ == "__main__":
    unreliable_api_simulator()
```

This Python script sets up a simple socket server that simulates an unreliable API. It accepts connections and, with a 40% chance, closes them immediately without sending any data. With a 60% chance, it sends back a random string of nonsensical data. The program is self-contained and has clear comments explaining its functionality.