import pickle

from flask import Flask
from model_training import preping_data


def create_app():
    app = Flask(__name__)
    app.model = pickle.load(open(
        '/Users/basti/Downloads/UCB-MFE-python-preprogram/Homeworks/HW9/bastien_gros/data/trained_model.pckl', 'rb'))
    app.data, _ = preping_data('sqlite:////Users/basti/Downloads/UCB-MFE-python-preprogram/data/data.db')
    return app


app = create_app()


@app.route("/")
def hello_world():
    return "<p>let's try this out !</p>"


@app.route("/health_check")
def alive():
    return "I'm alive !"

@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    ret_sol = app.model.predict(app.data.loc[time_stamp].to_frame().T)[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
