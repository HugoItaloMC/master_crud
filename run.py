from tornado import ioloop, httpserver
from routes import Routes

def main():
    http_server = httpserver.HTTPServer(Routes())
    http_server.listen(5000)
    ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()