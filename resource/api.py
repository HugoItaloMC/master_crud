from threading import RLock

from config.controller import APIMeta


class API(APIMeta):

    def __init__(self):
        super().__init__()
        self.lock = RLock()

    def __getattr__(self, item):
        return super().__getattr__(item)

    def post(self, body):

        with self.lock:
            self.produce.create_table()
            self.produce.fname = body.get('fname')
            self.produce.lname = body.get('lname')
            self.produce.size = int(body.get('size'))
            self.produce.poster()

    def put(self, body):

        with self.lock:
            id = int(body.get("id"))
            self.produce.fname = body.get("fname")
            self.produce.lname = body.get("lname")
            self.produce.size = body.get("size")
            self.produce.put(id=id)

    def getall(self):
        return self.produce.geter()

    def getter(self, body):
        return self.produce.getan(body)

    def remove(self, body):
        return self.produce.delete(body["id"])
