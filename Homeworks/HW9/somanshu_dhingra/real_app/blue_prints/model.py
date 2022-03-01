from flask import Blueprint, current_app


model_routes = Blueprint("model_routes", __name__)


@model_routes.route("/predict/<string:time_stamp>")
def predict_returns(time_stamp: str):
    # time stamp should be of the form: "2021-11-01"
    pred_ret = current_app.config['model'].predict(
        current_app.config['data'].loc[time_stamp].to_frame().T
    )[0]
    return {"excess_Unilever_return": pred_ret}
    