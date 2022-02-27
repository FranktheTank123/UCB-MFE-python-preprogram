import pickle

from flask import Flask
from model_training import preping_data
import numpy as np

def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/lenovo/git_intro/HW9/Dongyu_Wei/data/model.pickle', 'rb'))
    # this is not the best way to do it
    # app.data = X
    app.X_train,app.X_test,app.y_train,app.y_test = preping_data('iris')
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:index>")
def predict_rel_sol(index: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(
       np.array([app.X_test[int(index)]])
    )[0]
    ret_sol = max(round(ret_sol),0)
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
