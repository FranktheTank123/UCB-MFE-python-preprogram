import pickle

from flask import Flask
from model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/alexmccall/pythonProjects/MFEPY9/alex_mccall/data/best_model.pkl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    app.data, _ = preping_data('/Users/alexmccall/pythonProjects/MFEPY9/alex_mccall/data/returns1.csv')
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:time_stamp>")
def predict_ret_GSPC(time_stamp: str):
    # time stamp should be of the form: "2021-11-01"
    ret_GSPC = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_GSPC": ret_GSPC}


if __name__ == '__main__':
    app.run("localhost", port=5000)
