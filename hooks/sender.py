from flask import request, jsonify
from resource.api import API


def sender_header(content_type):
    METHOD_2INSERT = ['POST', 'PUT', 'DELETE']  # Is content constant,  methods way for insert data
    PATH_2GET = ['home', 'product']  # Path's to response data

    api = API()  # Requests & Responses
    xstr = lambda ss: ss or ""  # Believe it content
    content_json = "json" in xstr(content_type)  # Statement to base case

    # Verbose HTTP context
    while op := request.method:  # Required Method
        if op in METHOD_2INSERT:  # Do Condition from request
            for line in METHOD_2INSERT:  # Iterator in constant

                #  Running context To json data
                while line == op:
                    label = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                    fields = request.json if content_json else label
                    return api.post(body=fields) if op == 'POST' else api.put(body=fields) if op == 'PUT' else api.remove(body=fields)  # Base case condition

        elif op == 'GET':
            for line in PATH_2GET:
                while line in finder_url_path():
                    try:
                        return jsonify(
                            {"STATUS": 200,
                             "data": api.getall()}

                        ) if line == 'home' else jsonify(
                            {"STATUS": 200,
                             "data": api.getter(finder_url_id())})

                    except Exception as err:
                        return jsonify({"STATUS to error %s" % str(err): 500})


def finder_url_path():
    return request.path.split('/') if True else request.args


def finder_url_id():
    id = request.get_json()
    return id.get("id")
