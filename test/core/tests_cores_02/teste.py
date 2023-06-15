from functools import wraps

from flask import request, Flask, jsonify

app = Flask(__name__)


def fields_get(methods="*", out="fields"):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            xstr = lambda s: s or ""
            contentJson = "json" in xstr(request.headers.get("Content-Type"))

            if methods == "*" or request.method in methods:
                if request.method == "GET":
                    fields = request.args.to_dict()
                elif request.method in ["POST", "PUT", "DELETE", "DEL", "CREDIT"]:
                    data = request.get_json(force=True) or request.get_json() or request.form.to_dict()
                    fields = request.json if contentJson else data

                kwargs[out] = fields
                result = function(*args, **kwargs)
                return result
            else:
                kwargs[out] = []
                return function(*args, **kwargs)

        return wrapper

    return decorator


@app.route('/test', methods=['POST'])
@fields_get()
def test(fields):
    nome = fields.get('nome')
    idade = fields.get('idade')

    response = {
        'nome': nome,
        'idade': idade
    }

    return jsonify({"results": response})
