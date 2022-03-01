import pickle

from flask import Flask
from .model_training import preping_data


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/alvinyu/MFE_Preprogram/UCB-MFE-python-preprogram/Homeworks/HW9/Alvin_Yu/data/trained_model.pckl', 'rb'))
    app.data, _ = preping_data('sqlite:////Users/alvinyu/MFE_Preprogram/UCB-MFE-python-preprogram/Homeworks/HW9/Alvin_Yu/data/data.db')
    return app


app = creat_app()


@app.route("/")
def Model_Generator():
    return "<p>I will predict price of Solano at a given time. Go to /Help for details.</p>"


@app.route("/Help")
def HelpMessage():
    return "<p>time stamp should be of the form: 2021-11-01_00:00:00<p>"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    ret_sol = app.model.predict(
        app.data.loc[time_stamp.replace("_"," ")].values.reshape(1, -1)
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
