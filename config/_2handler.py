from tornado import httputil
from tornado.web import RequestHandler
from app.model import Calcados

class Index(RequestHandler):

    def __init__(self, application: "Application", request: httputil.HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)

    def home_2handler(self):
        self.render('index.html', produto=None)

    def new_2handler(self):
        self.render('new.html')

    def update_2handler(self):
        self.render('update.html')
