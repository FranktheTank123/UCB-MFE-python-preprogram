from flask import Flask
from blue_prints.boo import boo_routes
from blue_prints.foo import foo_routes


def creat_app():
    app = Flask(__name__)
    app.register_blueprint(boo_routes)
    app.register_blueprint(foo_routes)
    return app


if __name__ == '__main__':
    app = creat_app()
    app.run("localhost", port=5000)
