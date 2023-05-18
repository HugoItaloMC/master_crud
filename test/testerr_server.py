#  Server socket TCP to views/routes
import socket
import socketserver
import threading

from testerr_http_handler import HandlerHttp


class Netting:

    def __getattr__(self, item):
        value = item
        setattr(self, item, value)
        return value

    def sockparser(self):
        raise NotImplementedError


class TestServer(Netting):

    def sockparser(self):
        # Begin server bind in host from socket
        # Server create thread to client_socket

        if hasattr(self, 'target') and hasattr(self, 'port'):
            for res in socket.getaddrinfo(self.target, self.port,
                                          socket.AF_UNSPEC,
                                          socket.SOCK_STREAM,
                                          0,
                                          socket.AI_PASSIVE):
                af, socktype, proto, canonname, sa = res
            else:
                try:
                    with socketserver.TCPServer(sa, HandlerHttp) as httpd:
                        print('[*] - Listening on ', sa)
                        httpd.serve_forever()
                except TypeError as err:
                    print('Error : ', err)
                    print('[*] - Listening on : ', sa)


if __name__ == '__main__':

    server = TestServer()
    server.target = 'localhost'
    server.port = 8080

    # Test Thread : OK
    threads = []
    while not threads:
        thread = threading.Thread(target=server.sockparser)
        thread.start()
        threads.append(thread)

    for line in threads:
        line.join()
