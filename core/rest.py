from flask import request, jsonify

from core.handler import Handler
from resource.common import Method


class RestPost(Handler):
    _method = Method()

    def post(self):
        self._method(request.headers.get('Content-type'))
        return jsonify({"OK": 200})


class RestPut(Handler):

    _method = Method()

    def put(self):

        self._method(request.headers.get('Content-type'))
        return jsonify({"STATUS": 200})


class RestGetAll(Handler):
    _method = Method()

    def get(self):
        return self._method(request.headers.get("Content-type"))


class RestGetAn(Handler):
    _method = Method()

    def get(self):
        return self._method(request.headers.get("Content-type"))


class RestDelete(Handler):
    _method = Method()

    def delete(self):
        self._method(request.headers.get('Content-type'))
        return jsonify({"STATUS": 200})