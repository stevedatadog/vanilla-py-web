import http.server
import socketserver
import random
import logging

PORT = 5000

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
            logger.info(f"Served greeting")
        elif self.path == '/prime':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            prime = get_random_prime()
            self.wfile.write(f"Here's a prime number: {prime}".encode())
            logger.info(f"Served prime number {prime}")
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            prime = get_random_prime()
            self.wfile.write(f"Sorry, I can't find that.".encode())
            logger.error(f"{self.path} not found")

handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    logger.info(f"Starting Vanilla Py Web Server on {PORT}")
    httpd.serve_forever()

