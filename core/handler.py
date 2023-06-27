from flask_restx import Resource

from resource.api import API
from hooks.sender import sender_header


class Handler(Resource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = API()
        self.api.sender_header = sender_header
