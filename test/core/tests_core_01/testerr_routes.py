# End points to application
from tornado.web import Application

from test.tests_core.testerr_http_handler import (PostHandler,
                                                  PutHandler,
                                                  GetHandler,
                                                  GetanHandler)


class Routes(Application):
    # Insert resource in end-points from handlers

    def __init__(self):
        Application.__init__(self)
        handlers = [
            (r'/insert', PostHandler),
            (r'/update/(\d+)', PutHandler),
            (r'/home', GetHandler),
            (r'/home/(\d+)', GetanHandler)
        ]
        Application.__init__(self, handlers)
