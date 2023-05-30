from tornado.web import Application
from app.main import Get, Post, Put, Delete


class Routes(Application):
    def __init__(self):

        handlers = [
            ('/home', Get),
            (r'/produto/new', Post),
            (r'/produto/update/(\d+)', Put),
            (r'/produto/delete/(\d+)', Delete)
        ]
        Application.__init__(self, handlers)
