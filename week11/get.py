import http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [{
    "name": "Sam Larry",
    "track": "AI Developer"
    
}]

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

        
    def do_GET(self):
        self.send_data(data)
       
