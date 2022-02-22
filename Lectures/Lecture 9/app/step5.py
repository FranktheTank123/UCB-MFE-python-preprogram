from flask import Flask, abort
import time


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()


@app.route("/")
def basic():
    return "<p>Hello, World!</p>"


@app.route('/<int:status>')
def show_status(status: int):
    return f'Asking status: {status}', status


@app.route('/abort/<int:status>')
def abort_(status: int):
    abort(status)
    # these lines will never be executed
    time.sleep(100000)


if __name__ == '__main__':
    app.run("localhost", port=5000)
