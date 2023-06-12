# The handler to http method
import json
from typing import Any

from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler

from test.tests_core.testerr_api import Method


class Handler(RequestHandler):
    # The config `request handler`
    def __init__(self, application: "Application",
                 request: HTTPServerRequest,
                 **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.api = Method()


class Post:

    def __set__(self, instance):
        return lambda request_body: instance.api.post(request_body)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__set__(instance)


class Put:

    def __set__(self, instance):

        def read_id(id):
            # Parser url to get `id`
            url_parser = instance.request.path.split('/')
            id_index = url_parser.index('update') + 1
            return url_parser[id_index]

        return lambda id: instance.api.put(instance.request.body, read_id(int(id)))

    def __get__(self, instance, owner):
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)


class GetAll:

    def __set__(self, instance):
        instance.set_header('Content-type', 'application/json')
        return lambda response: instance.write(response)

    def __get__(self, instance, owner):
        if instance is None: return self
        return self.__set__(instance)


class GetAn:

    def __set__(self, instance):
        def read_id(id):
            # Parser url to get `id`
            url_parser = instance.request.path.split('/')
            id_index = url_parser.index('home') + 1

            # Read database where id
            return instance.api.getter(url_parser[id_index])

        instance.set_header('Content-type',  'application/json')
        return lambda id: instance.write(read_id(int(id)))

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)


class PostHandler(Handler):
    _post = Post()

    def post(self):
        self._post(self.request.body)


class PutHandler(Handler):

    _put = Put()

    def put(self, id):
        self._put(id)


class GetHandler(Handler):
    _getall = GetAll()

    def get(self):
        self._getall(self.api.getall())


class GetanHandler(Handler):

    _getan = GetAn()

    def get(self, id):
        self._getan(id)


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
