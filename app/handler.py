from typing import Any

from tornado.httputil import HTTPServerRequest
from tornado.web import RequestHandler

from resource.api import API


class Handler(RequestHandler):

    def __init__(self, application: "Application", request: HTTPServerRequest, **kwargs: Any):
        super().__init__(application, request, **kwargs)
        self.api = API()
