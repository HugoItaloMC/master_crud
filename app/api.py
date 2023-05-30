import json

from app.model import Product
from abstract.pagine import APIMeta


class API(APIMeta):

    def __init__(self):
        super().__init__()
        self.__produce = Product()

    def __getattr__(self, attr):
        super().__getattr__(attr)

    # Methods follow http requests

    def _post(self, request_body):
        require = json.loads(request_body.decode('utf-8'))

        self.__produce.create_table()
        self.__produce.fname = require.get('fname')
        self.__produce.lname = require.get('lname')
        self.__produce.size = require.get('size')
        self.__produce.poster()

    def _put(self, request_body, id):
        require = json.loads(request_body.dedoce('utf-8'))

        self.__produce.fname = require.get('fname')
        self.__produce.lname = require.get('lname')
        self.__produce.size = require.get('size')
        self.__produce.put(id)

    def _get(self):
       ...

    def _getall(self):
        # Recuperar dados do DB
        require = self.__produce.geter()
        return json.dumps({"Data": require})

    def _remove(self, id):
        ...


if __name__ == '__main__':
    api = API()
    getter = api._getall()
    print(getter)
