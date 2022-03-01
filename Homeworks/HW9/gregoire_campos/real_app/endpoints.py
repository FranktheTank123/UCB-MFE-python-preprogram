import pickle

import pandas as pd
from flask import Flask

from compare_pipelines import compare_models
from model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(
        open(
            "/Users/campo/Desktop/MFEpython/Homeworks/HW9/gregoire_campos/data/trained_model.pckl",
            "rb",
        )
    )
    # this is not the best way to do it
    # app.data = X
    app.data, _ = preping_data(
        "sqlite:////Users/campo/Desktop/MFEpython/Homeworks/HW9/gregoire_campos/data/data.db"
    )
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<head><link rel='shortcut icon' href='#'></head><p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/data")
def display_data():
    return app.data.to_html()

@app.route("/pipelines")
def comparison():
    # takes a few minutes to process
    df = compare_models()
    df = pd.DataFrame(df.values(), df.keys(), columns=["model performance"])
    return df.to_html()


@app.route("/my_name_is")
def pang():
    return "Grégoire"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(app.data.loc[time_stamp].to_frame().T)[0]
    return {"ret_sol": ret_sol, "chosen_model": str(app.model)}


if __name__ == "__main__":
    app.run("localhost", port=5000)
