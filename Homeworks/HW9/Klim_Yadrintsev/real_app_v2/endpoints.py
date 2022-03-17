import pickle
import pandas as pd
from model_training import preping_data

from flask import Flask


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('data_v2/model.pkl', 'rb'))
    data_location = 'sqlite:///data_v2/avocado.db'
    app.data, _ = preping_data(data_location)
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:time_stamp>-<string:region>")
def predict_price_avc(time_stamp: str, region: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"

    datacl = app.data[app.data.Date == '2015-12-06']
    datacll = datacl[datacl.region == 'Albany'].where(datacl.type == 'conventional').dropna()

    price = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"price": price}

    # price = app.model.predict(
    #     app.data.loc[time_stamp].to_frame().T
    # )[0]
    # return {"price": price}


if __name__ == '__main__':
    app.run("localhost", port=5000)

