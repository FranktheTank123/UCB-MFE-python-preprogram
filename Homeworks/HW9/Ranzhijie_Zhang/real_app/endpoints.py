import pickle

from flask import Flask
from model_training import preping_data
import numpy as np


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('~/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Ranzhijie_Zhang/data/trained_model.pckl', 'rb'))

    app.X,app.Y = preping_data('sqlite:///~/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Ranzhijie_Zhang/data/data.db')
    return app


app = creat_app()

@app.route("/predict"):
    return app.model.


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"





if __name__ == '__main__':
    app.run("localhost", port=5000)
