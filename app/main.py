from tornado.web import RequestHandler
from app.api import API

api = API()

class Get(RequestHandler):
    ...

class Post(RequestHandler):
    ...


class Put(RequestHandler):
    ...


class Delete(RequestHandler):
    ...
