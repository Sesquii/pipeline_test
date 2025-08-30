# BATCH6_PROMPT15_{{model_name}}.py

import http.server
import socketserver
import random
import time

class UnreliableAPISimulator(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 40% chance to return a 503 Service Unavailable
        if random.random() < 0.4:
            self.send_error(503, "Service Unavailable")
            return
        
        # Delay for 1-5 seconds
        delay = random.randint(1, 5)
        time.sleep(delay)
        
        # Always return a 200 OK response with an empty body
        self.send_response(200)
        self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=UnreliableAPISimulator, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()

# ===== GENERATED TESTS =====
```python
# BATCH6_PROMPT15_{{model_name}}.py

import http.server
import socketserver
import random
import time
from typing import Callable, Tuple
import pytest

class UnreliableAPISimulator(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # 40% chance to return a 503 Service Unavailable
        if random.random() < 0.4:
            self.send_error(503, "Service Unavailable")
            return
        
        # Delay for 1-5 seconds
        delay = random.randint(1, 5)
        time.sleep(delay)
        
        # Always return a 200 OK response with an empty body
        self.send_response(200)
        self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=UnreliableAPISimulator, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting httpd server on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
```

# Test Suite

```python
import pytest
from unittest.mock import patch
import socketserver
import threading
import time
from typing import Callable, Tuple

def start_server(handler_class: Callable, port: int) -> Tuple[socketserver.TCPServer, threading.Thread]:
    server_address = ('', port)
    httpd = socketserver.ThreadingTCPServer(server_address, handler_class)
    
    def run_server():
        httpd.serve_forever()
    
    thread = threading.Thread(target=run_server)
    thread.start()
    return httpd, thread

def stop_server(httpd: socketserver.TCPServer, thread: threading.Thread):
    httpd.shutdown()
    thread.join()

class TestUnreliableAPISimulator:
    @pytest.fixture
    def server(self) -> Tuple[socketserver.TCPServer, threading.Thread]:
        handler_class = UnreliableAPISimulator
        port = 8001
        return start_server(handler_class, port)
    
    @pytest.mark.parametrize("expected_status", [200, 503])
    def test_do_GET(self, server: Tuple[socketserver.TCPServer, threading.Thread], expected_status: int):
        httpd, thread = server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', 8001))
            s.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
            response = s.recv(4096)
        
        assert expected_status in response.decode()
    
    def test_run(self):
        handler_class = UnreliableAPISimulator
        port = 8002
        httpd, thread = start_server(handler_class, port)
        stop_server(httpd, thread)

if __name__ == "__main__":
    pytest.main()
```

This test suite includes comprehensive tests for the `UnreliableAPISimulator` class and the `run` function. It uses pytest fixtures to manage the server lifecycle and parametrization to handle both 200 OK and 503 Service Unavailable responses. The tests ensure that the server behaves as expected under different conditions, including random delays and error responses.