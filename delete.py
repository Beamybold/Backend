from http.server import BaseHTTPRequestHandler, HTTPServer
import json

data = [
    {
        "name": "Sam Larry",
        "track": "AI Developer"
    }
]

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status = 200):
        self.end_headers(status)
        self.wfile.write(json.dumps(payload).encode())

    def do_DELETE(self):
        content_size = int(self.headers.get("Content-Length", 0))
        put_data = self.rfile.read(content_size)
        remove_data = json.loads(put_data)
        user = remove_data.get("name")

        for record in data:
            if record["name"] == user:
                data.remove(record)
                self.send_data({
                    "message": "Record removed",
                    "data": record
                })
                return
        self.send_data({"Error: Record not found"}, status =404)
        

def run():
    HTTPServer(('localhost', 8000), BasicAPI).serve_forever()

print("Application is running")