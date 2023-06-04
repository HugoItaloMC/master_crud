from app.handler import Handler
from resource.common import Post, Put, GetAn, GetAll


class RestPost(Handler):
    _post = Post()

    def post(self):
        # Post
        self._post(self.request.body)


class RestPut(Handler):
    _put = Put()

    def put(self, id):
        self._put(id)


class RestGetAll(Handler):
    _getall = GetAll()

    def get(self):
        self._getall(self.api.getall())


class RestGetAn(Handler):
    _getan = GetAn()

    def get(self, id):
        self._getan(id)


class Delete(Handler):

    def delete(self, id):
        url_parser = self.request.path.split('/')
        id_index = url_parser.index('produto') + 2
        id = int(url_parser[id_index])

        # Drop Data
        self.api.remove(id)