from flask import Blueprint


boo_routes = Blueprint("boo", __name__)


@boo_routes.route('/boo')
def hello_world():
    return "this is boo's hello world"
