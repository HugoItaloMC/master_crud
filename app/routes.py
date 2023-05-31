from tornado.web import Application
from app.main import Getter, Post, Put, Delete, Getan


class Routes(Application):
    def __init__(self):

        handlers = [
            (r'/home', Getter),
            (r'/home/(\d+)', Getan),
            (r'/produto/new', Post),
            (r'/produto/update/(\d+)', Put),
            (r'/produto/delete/(\d+)', Delete)
        ]
        Application.__init__(self, handlers)
