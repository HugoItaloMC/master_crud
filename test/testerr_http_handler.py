# The handler to http method
import http.server
import json
import urllib.parse

from http.server import BaseHTTPRequestHandler
from socketserver import BaseServer

from testerr_api import Method


class HandlerHttp(BaseHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: tuple[str, int], server: BaseServer):
        super().__init__(request, client_address, server)
        self._headers_buffer = []

    def do_POST(self):

        # POST >>
        try:
            if self.path == '/insert':
                # Read Body request by Json POST
                length_util = int(self.headers['content-Length'])
                content_body = self.rfile.read(length_util)

                # Insert data from api method for database and upload to json
                self.api = Method()
                self.api.post(content_body)

                # Response Header's
                data_require = {'message': 'Sucedfull Insert to DataBase '}
                response = json.dumps(data_require).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Content-length', len(response))
                self.end_headers()
                self.wfile.write(response)

            # PUT >>
            elif self.path.startswith('/update/'):
                # Obter ID pelo end-point
                id = int(urllib.parse.urlparse(self.path).path.split('/')[-1])
                length_util = int(self.headers['content-length'])
                content_body = self.rfile.read(length_util)

                self.api = Method()
                self.api.put(content_body, id)

                data_require = {'message': 'Sucedfull Insert to DataBase '}
                response = json.dumps(data_require).encode('utf-8')
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Content-length', len(response))
                self.end_headers()
                self.wfile.write(response)
        except Exception as err:
            if err == self.send_error(501):
                self.send_response_only(501, message='error, %s not implemented error' % err)



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
