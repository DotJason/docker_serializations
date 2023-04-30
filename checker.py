from http.server import HTTPServer, BaseHTTPRequestHandler
import timeit


data = {
    'integer': 123456789,
    'float': 3.14,
    'string': 'Hello World!',
    'array': [123, 7.5, 'test'],
    'dict': {
        'grass': 'hopper',
        'green': 'grass'
    },
    'None': None,
    'empty_string': '',
    'big_array': [i for i in range(1000)]
}


def run_checker_server(format_name, serialize_func, deserialize_func, port):
    class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            serialized_data = serialize_func(data)
            serialized_data_size = len(serialized_data)

            serialize_time = timeit.timeit(lambda: serialize_func(data), number=1000)
            deserialize_time = timeit.timeit(lambda: deserialize_func(serialized_data), number=1000)

            response = f'{format_name} - {serialized_data_size} - {serialize_time}ms - {deserialize_time}ms\n'

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()

            self.wfile.write(bytes(response, 'utf-8'))

    httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
    httpd.serve_forever()
