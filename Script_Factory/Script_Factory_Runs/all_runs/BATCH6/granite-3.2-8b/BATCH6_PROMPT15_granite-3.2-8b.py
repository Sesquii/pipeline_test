# BATCH6_PROMPT15_Granite.py

import http.server
import socketserver
import random
from time import sleep

class UnreliableAPIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if random.random() < 0.6:
            self.send_response(200)
            self.end_headers()
        else:
            self.send_error(503, 'Service Unavailable')
            delay = random.randint(1, 5)
            sleep(delay)

def run(server_class=http.server.HTTPServer, handler_class=UnreliableAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting httpd on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()