from flask_restful import reqparse, Resource

from testerr_api import API


class Handler(Resource):

    def __init__(self):
        super(__class__, self).__init__()
        self.api = API()


class PostHandler(Handler):
    ...


class PutHandler(Handler):
    ...


class GetHandler(Handler):
    ...


class GetanHandler(Handler):
    ...