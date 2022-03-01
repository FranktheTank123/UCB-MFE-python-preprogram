import pickle

import jsonschema
import numpy as np
import pandas as pd
from flasgger import Swagger
from flask import Flask, abort, request
from model_training import preping_data
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit, cross_validate


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(
        open("/Users/Siyuan Fan/myproject/data/trained_model.pckl", "rb")
    )
    app.data, _ = preping_data("sqlite:////Users/Siyuan Fan/myproject/data/data.db")
    app.swagger = Swagger(app)
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    """
    Indicates that the server is up
    ---
    tags: [health_check]
    responses:
        200:
            description: Server is up
        400:
            description: Server is down
    """
    return "pong"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    """
    Predict ret_SOL
    ---
    tags: [predict]
    parameters:
      - name: time_stamp
        in: path
        type: string
        required: True
    responses:
        200:
            description: Prediction is made
    """
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(app.data.loc[time_stamp].to_frame().T)[0]
    return {"ret_sol": ret_sol}


@app.route("/abort/<int:status>")
def abort_(status: int):
    abort(status)


@app.route("/shape")
def shape():
    """
    Print the shape of the data
    ---
    tags: [shape]
    responses:
        200:
            description: Shape is printed
    """
    return f"app.data is of shape: {app.data.shape}"


@app.route("/ret_SOL")
def ret_sol():
    """
    Print ret_SOL
    ---
    tags: [ret_SOL]
    responses:
        200:
            description: Summary of ret_SOL is printed
    """
    return f"ret_sol: {app.data.ret_SOL.shift(-1)[:-1].describe()}"


@app.route("/count_null")
def cout_null():
    """
    Count number of null values in the data
    ---
    tags: [count null]
    responses:
        200:
            description: number of null is printed
    """
    return f"number of null in data: {pd.isnull(app.data).sum()}"


@app.route("/correlation")
def correlation():
    """
    Print correlations of ret_SOL vs. each variable
    ---
    tags: [correlations]
    responses:
        200:
            description: correlations are printed
    """
    y = app.data.ret_SOL.shift(-1)[:-1]
    X = app.data[:-1]
    return {col: y.corr(X[col]) for col in X.columns if X[col].dtype != "object"}


@app.route("/RMSE")
def rmse():
    """
    Print average cross-validated RMSE
    ---
    tags: [RMSE]
    responses:
        200:
            description: Average cross-validated RMSE is printed
    """
    test_size = 0.2
    y = app.data.ret_SOL.shift(-1)[:-1]
    X = app.data[:-1]
    model = app.model
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    return f"Average Cross-validated RMSE: {np.mean(cross_validate(model, X, y, cv=cv, scoring=scorer, n_jobs=-1)['test_score'])}"


if __name__ == "__main__":
    app.run("localhost", port=5000)
