# End points to application
from tornado.web import Application

from testerr_http_handler import PostHandler, PutHandler


class Routes(Application):
    # Insert behaviours in end-points from handlers

    def __init__(self):
        Application.__init__(self)
        handlers = [
            (r'/insert', PostHandler),
            (r'/update/(\d+)', PutHandler),
        ]
        Application.__init__(self, handlers)

    def __iter__(self):
        yield from {
            "post": PostHandler.__bases__,
            "put": PutHandler.__bases__}

    def __dict__(self):
        return next(self.__iter__())


if __name__ == '__main__':
    import unittest

    class TestsRoutes(unittest.TestCase):

        def tests_instances(self):

            app = Routes()
            self.assertEquals(app, Routes)
    unittest.main()

