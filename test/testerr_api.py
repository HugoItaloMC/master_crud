import json
from threading import Lock

from tests_model.testerr_model import Product


class Descriptor:
    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value

    def method(self):
        raise NotImplementedError


class Method(Descriptor):

    def __init__(self):
        self.__produce = Product()
        self.lock = Lock()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def post(self, request_body):
        with self.lock:
            require = json.loads(request_body.decode('utf-8'))

            self.__produce.create_table()
            self.__produce.fname = require.get('fname')
            self.__produce.lname = require.get('lname')
            self.__produce.size = int(require.get('size'))
            self.__produce.poster()

    def put(self, request_body, id):
        with self.lock:
            require = json.loads(request_body.decode('utf-8'))

            self.__produce.fname = require.get('fname')
            self.__produce.lname = require.get('lname')
            self.__produce.size = require.get('size')
            self.__produce.put(id)