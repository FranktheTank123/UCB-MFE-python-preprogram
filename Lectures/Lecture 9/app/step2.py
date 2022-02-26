from flask import Flask


def creat_app():
    app = Flask(__name__)
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run("localhost", port=5000)
