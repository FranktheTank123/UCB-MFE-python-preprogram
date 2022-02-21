from flask import Blueprint
import pickle
import pandas as pd

def create_model_route():
    model = Blueprint("model", __name__)
    model.df = pd.read_csv("../data/data.csv", index_col=[0,1])
    model.df.pop("target")
    model.model = pickle.load(open("../data/base_model.pkl", "rb"))
    return model

model = create_model_route()

@model.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@model.route("/<int:time_id>/<int:investment_id>")
def predict(time_id, investment_id):
    try:
        target = model.model.predict(
            model.df.loc[time_id, investment_id].to_frame().T
        )[0]
        return {"predict result": target}
    except KeyError:
        target = f"time id:{time_id} or investment id:{investment_id} not found!"
        return {"Error": target}, 400

@model.route("/ping")
def ping():
    return "pong"
