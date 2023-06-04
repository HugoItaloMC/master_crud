from tornado.web import Application
from app.rest import RestPut, RestPost, RestGetAn, RestGetAll


class Routes(Application):

    def __init__(self):

        handlers = [
            (r'/home', RestGetAll),
            (r'/home/(\d+)', RestGetAn),
            (r'/produto/new', RestPost),
            (r'/produto/update/(\d+)', RestPut)
        ]
        Application.__init__(self, handlers)
