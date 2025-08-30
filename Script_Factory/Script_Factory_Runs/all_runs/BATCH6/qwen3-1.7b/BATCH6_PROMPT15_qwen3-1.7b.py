```python
import http.server
import socketserver
import random
import time

class UnreliableAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/api':
            if random.random() < 0.6:
                self.send_response(200)
                self.end_headers()
            else:
                delay = random.randint(1, 5)
                time.sleep(delay)
                self.send_response(503)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b"Service Unavailable")
        else:
            self.send_error(404, "Not Found")

def run_server():
    port = 8000
    server_address = ('', port)
    with socketserver.TCPServer(server_address, UnreliableAPIHandler) as httpd:
        print(f"Server running on port {port}...")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()