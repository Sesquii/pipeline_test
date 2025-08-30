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