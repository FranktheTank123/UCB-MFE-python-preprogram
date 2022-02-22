import os
import pickle

import pandas as pd
from flask import Flask, render_template
from model_training import load_data


def create_app():
    app = Flask(__name__)
    model_location = os.getcwd() + "/../data/trained_model.pckl"
    data_location = os.getcwd() + "/../data/chess_games_stats.csv"
    app.model = pickle.load(open(model_location, "rb"))
    app.data = load_data(data_location)

    return app


app = create_app()


@app.route("/")
def welcome():
    return "<p>Welcome!</p>"


@app.route("/ping")
def ping():
    return "pong"


"""
This endpoint takes a string of four rating values separated by underscores
i.e: games/1600_1660_1400_1430 (order: games/wi_lo_wi_hi_bl_lo_bl_hi)
and returns a neat table with all of the games in the data set that fall within the 
specified rating ranges for black and white. The purpose is to allow the user to 
find games within the ranges of greatest interest to them, note their game_ids, and
then access the model forecast for that game via another endpoint (see below).
"""


@app.route("/games/<string:rating_range>")
def get_games(rating_range: str):
    wi_lo, wi_hi, bl_lo, bl_hi = rating_range.split("_", 3)
    games_df = app.data.copy()
    games_df = games_df.loc[
        (games_df["White Rating"] >= int(wi_lo))
        & (games_df["White Rating"] <= int(wi_hi))
        & (games_df["Black Rating"] >= int(bl_lo))
        & (games_df["Black Rating"] <= int(bl_hi))
    ]

    return render_template(
        "display_table.html",
        column_names=games_df.columns.values,
        row_data=list(games_df.values.tolist()),
        zip=zip,
    )


"""
This endpoint takes a game id string and returns the (trained sklearn) model's 
forecast for the black centipawn loss in that game by calling the predict method.
"""


@app.route("/get_prediction/<string:game_id>")
def predict(game_id: str):
    fetch_game = app.data.loc[game_id].to_frame().T
    fetch_game["rating_diff"] = fetch_game["White Rating"] - fetch_game["Black Rating"]
    game = fetch_game[
        [
            "rating_diff",
            "White Centi-pawn Loss",
            "White's Number of Inaccuracies",
            "White's Number of Mistakes",
            "White's Number of Blunders",
        ]
    ]
    value = int(app.model.predict(game)[0])
    prediction_df = pd.DataFrame(
        data=[[game_id, value]], columns=["Game ID", "Predicted Black Centipawn Loss"]
    )

    return render_template(
        "display_table.html",
        column_names=prediction_df.columns.values,
        row_data=list(prediction_df.values.tolist()),
        zip=zip,
    )


"""
This endpoint takes a string of five values separated by underscores representing
the features trained by  this model i.e: forecast/61_14_1_1_2 
(order: forecast/rating_diff_white_centipawn_loss_white_inacc_
	white_mistakes_white_blunders)
and returns a neat table containing the forecasted black centipawn loss under the
specifications of this trained model (by calling predict using the user-specified
parameters). The purpose of this endpoint is to provide the user with the ability
to extrapolate the model and generate forecasts for hypothetical games not
found in the training data set.
"""


@app.route("/forecast/<string:forecast_string>")
def forecast(forecast_string: str):
    col = [
        "rating_diff",
        "White Centi-pawn Loss",
        "White's Number of Inaccuracies",
        "White's Number of Mistakes",
        "White's Number of Blunders",
    ]
    x_values = forecast_string.split("_", 4)
    test_x = pd.DataFrame(data=[x_values], columns=col)
    forecasted_value = int(app.model.predict(test_x)[0])
    forecast_df = pd.DataFrame(
        data=[["User Generated", forecasted_value]],
        columns=["Game ID", " Est. Black Centipawn Loss"],
    )

    return render_template(
        "display_table.html",
        column_names=forecast_df.columns.values,
        row_data=list(forecast_df.values.tolist()),
        zip=zip,
    )


if __name__ == "__main__":
    app.run("localhost", port=1324, debug=True)
