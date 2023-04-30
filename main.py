from http.server import HTTPServer, BaseHTTPRequestHandler
import requests


serializer_ports = {
    "pickle": 2001,
    "xml": 2002,
    "json": 2003,
    # "protobuf": 2004,
    # "avro": 2005,
    "yaml": 2006,
    "msgpack": 2007
}


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        port = serializer_ports.get(self.path[1:])

        if port is None:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(b'Incorrect query!\n')

            return

        r = requests.get(f'http://localhost:{port}/')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(r.content)


httpd = HTTPServer(('', 2000), SimpleHTTPRequestHandler)
httpd.serve_forever()
