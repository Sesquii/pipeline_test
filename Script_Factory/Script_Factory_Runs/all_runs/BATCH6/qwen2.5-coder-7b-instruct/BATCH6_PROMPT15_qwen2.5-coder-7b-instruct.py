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