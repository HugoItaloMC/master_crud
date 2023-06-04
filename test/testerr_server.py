from threading import Thread
# Server to APP
from tornado import ioloop, httpserver

from testerr_routes import Routes


def main():
    server = httpserver.HTTPServer(Routes())
    server.listen(5000)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()