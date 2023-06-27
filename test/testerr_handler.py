from flask import request, jsonify
from flask_restx import Resource

from testerr_api import API


def hook_path():
    return request.path.split('/') if True else request.args


def hook_id():
    id = request.get_json()
    return id.get("id")


def sender_header(content_type):
    METHOD_2INSERT = ['POST', 'PUT', 'DELETE']  # Is content constant,  methods way for insert data
    PATH_2GET = ['home', 'product']  # Path's to response data

    xstr = lambda ss: ss or ""  # Believe it content
    api = API()
    content_json = "json" in xstr(content_type)  # Statement to base case

    # Verbose HTTP context
    while op := request.method:  # Required Method
        if op in METHOD_2INSERT:  # Do Condition from request
            for line in METHOD_2INSERT:  # Iterator in constant

                #  Running context To json data
                while line == op:
                    label = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                    fields = request.json if content_json else label
                    # Base case condition
                    return api.post(fields) if op == 'POST' else api.put(fields) if op == 'PUT' else api.remove(body=fields)

        elif op == 'GET':
            for line in PATH_2GET:
                while line in hook_path():
                    try:
                        return jsonify(
                            {"STATUS": 200,
                             "data": api.getall()}

                        ) if line == 'home' else jsonify(
                            {"STATUS": 200,
                             "data": api.getter(hook_id())})

                    except Exception as err:
                        return jsonify({"STATUS to error %s" % str(err): 500})


class Method:
    def __set__(self, instance):
        return lambda content_type: instance.api.sender_header(content_type=content_type)

    def __get__(self, instance, owner):
        return self.__set__(instance)

    def __call__(self, *args):
        return self.__set__(args)


class Handler(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.api = API()
        self.api.sender_header = sender_header


class PostHandler(Handler):
    _method = Method()

    def post(self):

        self._method(request.headers.get('Content-type'))
        return jsonify({"OK": 200})


class PutHandler(Handler):
    _method = Method()

    def put(self):

        self._method(request.headers.get('Content-type'))
        return jsonify({"STATUS": 200})


class GetHandler(Handler):
    _method = Method()

    def get(self):
        return self._method(request.headers.get("Content-type"))


class GetanHandler(Handler):
    _method = Method()

    def get(self):
        return self._method(request.headers.get("Content-type"))


class DeleteHandler(Handler):
    _method = Method()

    def delete(self):
        self._method(request.headers.get('Content-type'))
        return jsonify({"STATUS": 200})