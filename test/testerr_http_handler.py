# The handler to http method
import json
from http.server import BaseHTTPRequestHandler
from socketserver import BaseServer

from testerr_repository import Api


class HandlerHttp(BaseHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: tuple[str, int], server: BaseServer):
        super().__init__(request, client_address, server)
        self._headers_buffer = []

    def do_POST(self):
        if self.path == '/home':
            # Read Body request by Json POST
            length_util = int(self.headers['content-Length'])
            content_body = self.rfile.read(length_util)

            # Upload data to jason
            require = json.loads(content_body.decode('utf-8'))

            # Insert data from api method for database
            self.api = Api()
            self.api.method(require)

            # Response Header's
            data_require = {'message': 'Sucedfull Insert to DataBase '}
            response = json.dumps(data_require).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Content-length', len(response))
            self.end_headers()
            self.wfile.write(response)



if __name__ == '__main__':
    import requests
    # Test request POST: OK
    data = {"fname": "nike", "lname": "camisa", "size": "33"}  # Data to request
    require = requests.post('http://localhost:8000/home', json=data)

    if require.status_code == 200:
        response_require = json.loads(require.content)
        print(response_require.get('message'))
    else:
        print("Error : ", require.status_code)
    print(type(HandlerHttp))
