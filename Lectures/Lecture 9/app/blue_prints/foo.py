from flask import Blueprint


foo_routes = Blueprint("foo", __name__)


@foo_routes.route('/foo')
def hello_world():
    return "this is foo's hello world"
