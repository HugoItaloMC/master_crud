import json
from threading import RLock

from flask import request

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

    def header(self, content_type):
        xstr = lambda ss: ss or ""
        content_json = "json" in xstr(content_type)
        while op := request.method:
            if op == 'POST':
                label = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                fields = request.json if content_json else label
                return self._post(fields)

    def _post(self, request_json):

        with self.lock:
            self.produce.create_table()
            self.produce.fname = request_json.get('fname')
            self.produce.lname = request_json.get('lname')
            self.produce.size = int(request_json.get('size'))
            self.produce.poster()

    def put(self, request_body, id):

        with self.lock:
            require = request_body.decode('utf-8')
            self.produce.fname = require.get("fname")
            self.produce.lname = require.get("lname")
            self.produce.size = require.get("size")
            self.produce.put(id=id)

    def getall(self):
        return json.dumps({'data': self.produce.geter()})

    def getter(self, id):
        return json.dumps({'data': self.produce.getan(id)})
