from tornado.web import Application
from app.main import Home, Post, Put, Delete

class Routes(Application):
    def __init__(self):

        handlers = [
            ('/home', Home),
            ('/produto/new', Post),
            ('/produto/update/(\d+)/id/(\d+)', Put),
            ('/produto/delete/(\d+)', Delete)
        ]

        settings = dict(
            debug=True,
            template_path='template',
            static_path='static',
        )

        Application.__init__(self, handlers, **settings)
