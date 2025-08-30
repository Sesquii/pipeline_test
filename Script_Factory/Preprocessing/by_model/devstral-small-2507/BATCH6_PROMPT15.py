import http.server
import random
import time
import threading

class UnreliableAPIHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # 60% chance to return 200 OK
        if random.random() < 0.6:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"")
        else:
            # 40% chance to return 503 Service Unavailable with delay
            delay = random.randint(1, 5)
            time.sleep(delay)
            self.send_response(503)
            self.end_headers()
            self.wfile.write(b"Service Unavailable")

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, UnreliableAPIHandler)
    print(f"Starting unreliable API simulator on port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    # Run the server in a separate thread to allow graceful shutdown
    server_thread = threading.Thread(target=run_server)
    server_thread.daemon = True
    server_thread.start()