from flask import Flask


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()


# ========================================
# Routing
# ========================================
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/boo')
def woo():
    return 'foo'


# ========================================
# Variable
# ========================================
@app.route('/name/<string:name>')  # we are using type converter here
def show_name(name):
    return f'Name {name}'


# ========================================
# HTTP methods
# ========================================
from flask import request


# by definition it's all `GET`
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "This is a POST method"
    else:
        return "This is a GET method"


# ========================================
# Return type as dict/JSON
# ========================================
@app.route('/json')
def json():
    return {'a': 1, 'b': 'x', 'c': 2.0}


# ========================================
# request body
# ========================================
@app.route('/request_body')
def request_with_body():
    return request.get_json(force=True)

# try with curl -X GET localhost:5000/request_body --data '{"a":1}'


if __name__ == '__main__':
    app.run("localhost", port=5000)
