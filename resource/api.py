from threading import RLock

from config.controller import APIMeta


class API(APIMeta):

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

    def getter(self, id):
        return self.produce.getan(id)

    def remove(self):
        ...
