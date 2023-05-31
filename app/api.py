import json

from config.resource import APIMeta


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
       require = self.produce.getan(id)
       return json.dumps({'data': require})

    def getall(self):
        # Recuperar dados do DB
        require = self.produce.geter()
        return json.dumps({"Data": require})

    def remove(self, id):
        require = self.produce.delete(id)
