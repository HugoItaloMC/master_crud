import json

from config.controller import APIMeta


class API(APIMeta):

    def __init__(self):
        super().__init__()

    def __getattr__(self, attr):
        super().__getattr__(attr)

    # Methods follow http requests
    def post(self, request_body):
        require = json.loads(request_body.decode('utf-8'))

        self.produce.create_table()
        self.produce.fname = require.get('fname')
        self.produce.lname = require.get('lname')
        self.produce.size = require.get('size')
        self.produce.poster()

    def put(self, request_body, id):
        require = json.loads(request_body.decode('utf-8'))

        self.produce.fname = require.get('fname')
        self.produce.lname = require.get('lname')
        self.produce.size = require.get('size')
        self.produce.put(id)

    def getter(self, id):
        return json.dumps({'data': self.produce.getan(id)})

    def getall(self):
        # Recuperar dados do DB
        return json.dumps({"Data": self.produce.geter()})

    def remove(self, id):
        require = self.produce.delete(id)
