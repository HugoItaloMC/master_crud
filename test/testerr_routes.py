from flask import Flask
from flask_restful import Api

from testerr_handler import (PostHandler, PutHandler, GetHandler, GetanHandler)
app = Flask(__name__)


class Router:

    def args_point(self):

        parser_router = Api(app)
        parser_router.add_resource(GetHandler, '/home')
        parser_router.add_resource(GetanHandler, '/home/<int:id>')
        parser_router.add_resource(PostHandler, '/insert')
        parser_router.add_resource(PutHandler, '/update/<int:id>')


begin = Router()
begin.args_point()
