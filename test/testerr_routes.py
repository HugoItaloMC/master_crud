from flask import Flask
from flask_restx import Api

from testerr_handler import PostHandler, PutHandler, GetHandler, GetanHandler, DeleteHandler
app = Flask(__name__)


class Router:
    @staticmethod
    def args_point():

        parser_router = Api(app)
        parser_router.add_resource(GetHandler, '/home', methods=['GET'])
        parser_router.add_resource(GetanHandler, '/product', methods=['GET'])
        parser_router.add_resource(PostHandler, '/insert', methods=['POST'])
        parser_router.add_resource(PutHandler, '/update', methods=['PUT'])
        parser_router.add_resource(DeleteHandler, '/delete', methods=['DELETE'])


begin = Router()
begin.args_point()
