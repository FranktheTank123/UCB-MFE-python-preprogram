from flask import Flask
from real_app.blue_prints import model

def create_app():
    app = Flask(__name__)
    app.register_blueprint(model)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run("localhost", port=5000)