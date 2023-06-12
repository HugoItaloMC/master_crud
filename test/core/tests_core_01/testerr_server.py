# Server to APP
from tornado import ioloop, httpserver

from test.tests_core.testerr_routes import Routes


def main():
    server = httpserver.HTTPServer(Routes())
    server.listen(5000)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()