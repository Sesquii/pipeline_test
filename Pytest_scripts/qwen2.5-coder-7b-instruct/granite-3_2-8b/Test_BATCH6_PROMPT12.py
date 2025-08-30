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

# ===== GENERATED TESTS =====
```python
# BATCH6_PROMPT12_{model_name}.py

import socket
import random
from unittest.mock import patch
import pytest

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

# Test suite for the script

def test_generate_nonsensical_data():
    """Test the generate_nonsensical_data function."""
    data = generate_nonsensical_data(10)
    assert len(data) == 10
    assert all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()' for char in data)

def test_handle_client_close_connection():
    """Test the handle_client function with a connection to close."""
    with patch('socket.socket') as mock_socket:
        client_socket = mock_socket.return_value
        client_socket.getpeername.return_value = ('127.0.0.1', 54321)
        random.random.return_value = 0.3  # Simulate closing connection

        handle_client(client_socket)

        assert client_socket.close.called

def test_handle_client_send_nonsense():
    """Test the handle_client function with a connection to send nonsensical data."""
    with patch('socket.socket') as mock_socket:
        client_socket = mock_socket.return_value
        client_socket.getpeername.return_value = ('127.0.0.1', 54321)
        random.random.return_value = 0.6  # Simulate sending nonsensical data

        handle_client(client_socket)

        assert client_socket.sendall.called
        sent_data = client_socket.sendall.call_args[0][0].decode()
        assert len(sent_data) == 10
        assert all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()' for char in sent_data)

def test_handle_client_exception():
    """Test the handle_client function with an exception."""
    with patch('socket.socket') as mock_socket:
        client_socket = mock_socket.return_value
        client_socket.getpeername.return_value = ('127.0.0.1', 54321)
        random.random.return_value = 0.8  # Simulate exception

        with pytest.raises(Exception):
            handle_client(client_socket)

def test_main():
    """Test the main function."""
    with patch('socket.socket') as mock_socket:
        s = mock_socket.return_value
        s.bind.return_value = None
        s.listen.return_value = None
        s.accept.side_effect = [((mock_socket(), ('127.0.0.1', 54321)), None), ((mock_socket(), ('127.0.0.1', 54322)), None)]

        main()

        assert s.bind.called
        assert s.listen.called
        assert s.accept.call_count == 2
```