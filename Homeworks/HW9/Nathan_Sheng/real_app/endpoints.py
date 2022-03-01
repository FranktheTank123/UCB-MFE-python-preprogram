import pickle

from flask import Flask
from model_training import get_data


def create_app():
    app = Flask(__name__)
    app.model = pickle.load(open("../data/model.pckl", "rb"))
    app.data, _ = get_data()
    return app


app = create_app()


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=8888)