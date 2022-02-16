import pickle

from flask import Flask
from model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    app.data, _ = preping_data('sqlite:////Users/tianyixia/dev/UCB-MFE-python-preprogram/data/data.db')
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
