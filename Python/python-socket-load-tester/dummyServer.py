from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, you reached the server!")

server = HTTPServer(('127.0.0.1', 8080), SimpleHandler)
print("Server running at http://127.0.0.1:8080")
server.serve_forever()
