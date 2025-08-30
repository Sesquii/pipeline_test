import socket
import random

class UnreliableAPISimulator:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port

    def generate_random_string(self, length=10):
        """Generate a random string of nonsensical data."""
        letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        return ''.join(random.choice(letters) for _ in range(length))

    def handle_client(self, conn):
        """Handle a client connection."""
        # 40% chance to close connection immediately
        if random.random() < 0.4:
            print("Connection closed immediately")
            conn.close()
            return

        # 60% chance to send random nonsensical data
        random_data = self.generate_random_string()
        print(f"Sending: {random_data}")
        conn.sendall(random_data.encode())
        conn.close()

    def run(self):
        """Run the unreliable API simulator."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")

            while True:
                conn, addr = s.accept()
                print(f"Accepted connection from {addr}")
                self.handle_client(conn)

if __name__ == "__main__":
    # Create and run the unreliable API simulator
    api_simulator = UnreliableAPISimulator()
    api_simulator.run()