from flask import Flask
from flask_restx import Api

from core.rest import RestPut, RestPost, RestGetAn, RestGetAll, RestDelete
app = Flask(__name__)


class Router:

    @staticmethod
    def args_point():
        parser_router = Api(app)
        parser_router.add_resource(RestGetAll, '/home', methods=['GET'])
        parser_router.add_resource(RestGetAn, '/product', methods=['GET'])
        parser_router.add_resource(RestPost, '/insert', methods=['POST'])
        parser_router.add_resource(RestPut, '/update', methods=['PUT'])
        parser_router.add_resource(RestDelete, '/delete', methods=['DELETE'])


begin = Router()
begin.args_point()
