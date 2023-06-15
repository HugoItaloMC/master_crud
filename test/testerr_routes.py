from flask import Flask
from flask_restx import Api

from testerr_handler import (PostHandler, PutHandler, GetHandler, GetanHandler)
app = Flask(__name__)


class Router:
    @staticmethod
    def args_point():

        parser_router = Api(app)
        parser_router.add_resource(GetHandler, '/home')
        parser_router.add_resource(GetanHandler, '/home/<int:id>')
        parser_router.add_resource(PostHandler, '/insert', methods=['POST'])
        parser_router.add_resource(PutHandler, '/update/<int:id>', methods=['PUT'])


begin = Router()
begin.args_point()
