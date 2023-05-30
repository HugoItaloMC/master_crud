# The handler to http method
from typing import Any

import tornado.web
from tornado import httputil
from tornado.web import RequestHandler

from testerr_api import Method


class PostHandler(RequestHandler):

    def __init__(self, application: "Application", request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.api = Method()

    def post(self):
        # Read content request:
        content_body = self.request.body

        # Insert data by API methods from JSON body
        self.api.post(content_body)


class PutHandler(RequestHandler):

    def __init__(self, application: "Application", request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.api = Method()

    def put(self, id):
        # Read content request
        content_body = self.request.body
        url_parse = self.request.path.split('/')
        id_index = url_parse.index('update') + 1
        id = int(url_parse[id_index])

        # Update data where id in database
        self.api.put(content_body, id=id)


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

