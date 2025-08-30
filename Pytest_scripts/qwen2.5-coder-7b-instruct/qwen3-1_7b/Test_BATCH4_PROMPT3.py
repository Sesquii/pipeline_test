```python
import http.server
import socketserver
import random

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if random.random() < 0.5:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "message": "API called successfully"}')
        elif random.random() < 0.3:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Internal Server Error')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"random_key": "abc"}')

def run():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()

# ===== GENERATED TESTS =====
```python
import pytest
from unittest.mock import patch
import requests

# Original code
class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if random.random() < 0.5:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "message": "API called successfully"}')
        elif random.random() < 0.3:
            self.send_response(500)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Internal Server Error')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"random_key": "abc"}')

def run():
    PORT = 8000
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Server running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run()
# End of original code

# Test cases
@pytest.fixture(scope="module")
def server():
    import threading
    from http.server import HTTPServer, BaseHTTPRequestHandler
    
    class MockHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "success", "message": "API called successfully"}')

    server = HTTPServer(('localhost', 8001), MockHandler)
    thread = threading.Thread(target=server.serve_forever)
    thread.start()
    
    yield server
    
    server.shutdown()
    thread.join()

def test_success_response(server):
    """Test the successful response from the server."""
    response = requests.get('http://localhost:8001')
    assert response.status_code == 200
    assert response.json() == {"status": "success", "message": "API called successfully"}

def test_error_response(server):
    """Test the error response from the server."""
    with patch.object(MyHandler, 'do_GET', side_effect=lambda *args: None) as mock:
        response = requests.get('http://localhost:8001')
        assert response.status_code == 500
        assert response.text == 'Internal Server Error'

def test_random_response(server):
    """Test the random response from the server."""
    with patch.object(MyHandler, 'do_GET', side_effect=lambda *args: None) as mock:
        response = requests.get('http://localhost:8001')
        assert response.status_code == 200
        assert 'random_key' in response.json()
```