from flask import request, jsonify
from flask_restx import Resource

from testerr_api import API


class Method:
    def __set__(self, instance):
        return lambda content_type: instance.api.header(content_type=content_type)

    def __get__(self, instance, owner):
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)


class Handler(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = API()

class PostHandler(Handler):
    _method = Method()
    def post(self):
        self._method(request.headers.get('Content-type'))


class PutHandler(Resource):
    ...


class GetHandler(Resource):
    ...


class GetanHandler(Resource):
    ...
