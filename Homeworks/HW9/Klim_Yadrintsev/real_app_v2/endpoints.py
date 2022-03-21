import pickle
import pandas as pd
from model_training import preping_data
from model_training import data_prep_prediction

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


@app.route("/<string:time_stamp>-<string:region>-<string:type_of>")
def predict_price_avc(time_stamp: str, region: str, type_of: str):
    # time stamp should be of the form: "2015-12-06"

    datacl = app.data[app.data.Date == time_stamp]
    datacll = datacl[datacl.region == region].where(datacl.type == type_of).dropna()
    fitted_datacll = [data_prep_prediction('sqlite:///data_v2/avocado.db').testflights[datacll.index[0]]]

    price = app.model.predict(
        fitted_datacll
    )[0]
    return {"price": price}

    # price = app.model.predict(
    #     app.data.loc[time_stamp].to_frame().T
    # )[0]
    # return {"price": price}


if __name__ == '__main__':
    app.run("localhost", port=5001)

