import json
from threading import RLock

from flask import request, jsonify

from tests_model_01.testerr_model import Product


class APIAsset:
    # The Config API

    def __init__(self):
        self.produce = Product()

    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value


class API(APIAsset):

    def __init__(self):
        super().__init__()
        self.lock = RLock()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def post(self, request_json):

        with self.lock:
            self.produce.create_table()
            self.produce.fname = request_json.get('fname')
            self.produce.lname = request_json.get('lname')
            self.produce.size = int(request_json.get('size'))
            self.produce.poster()

    def put(self, request_json):

        with self.lock:
            id = int(request_json.get("id"))
            self.produce.fname = request_json.get("fname")
            self.produce.lname = request_json.get("lname")
            self.produce.size = request_json.get("size")
            self.produce.put(id=id)

    def getall(self):
        return self.produce.geter()

    def getter(self, body):
        return self.produce.getan(body['id'])

    def remove(self, body):
        return self.produce.delete(body['id'])
