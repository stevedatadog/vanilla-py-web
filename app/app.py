import http.server
import socketserver
import random

PORT = 5000

def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_random_prime():
    """Get a random prime number."""
    while True:
        num = random.randint(1000, 10000)
        if is_prime(num):
            return num

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Vanilla Py Web OK! Make me do some work at prime/")
        elif self.path == '/prime':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            prime = get_random_prime()
            self.wfile.write(f"Here's a prime number: {prime}".encode())

handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()

