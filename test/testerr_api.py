import json
from io import StringIO
from threading import RLock

from tests_model.testerr_model import Product


class LazyAttr:

    def __init__(self):
        self.produce = Product()

    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value


class Method(LazyAttr):

    def __init__(self):
        super().__init__()
        self.lock = RLock()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def post(self, request_body):
        with self.lock:
            require = json.loads(request_body.decode('utf-8'))

            self.produce.create_table()
            self.produce.fname = require.get('fname')
            self.produce.lname = require.get('lname')
            self.produce.size = int(require.get('size'))
            self.produce.poster()

    def put(self, request_body, id):

        with self.lock:
            require = json.loads(request_body.decode('utf-8'))
            self.produce.fname = require.get("fname")
            self.produce.lname = require.get("lname")
            self.produce.size = require.get("size")
            self.produce.put(id=id)

    def getall(self):
        return json.dumps({'data': self.produce.geter()})

    def getter(self, id):
        return json.dumps({'data': self.produce.getan(id)})
