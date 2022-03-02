import pickle

from flask import Flask
from model_training import prepare_data


def create_app():
    app = Flask(__name__)
    app.model = pickle.load(open(
        "D:/MFE/Python/Session9/Homework/UCB-MFE-python-preprogram/Homeworks/HW9/Jianhao_Cai/data/train_model.pckl",
        "rb"))
    app.data, _, app.dict = prepare_data(
        "D:/MFE/Python/Session9/Homework/UCB-MFE-python-preprogram/Homeworks/HW9/Jianhao_Cai/data/data.xlsx")
    return app


app = create_app()


@app.route("/")
def hello():
    return "<p>Hello!</p>"


@app.route("/<string:inflow>")
def predict(inflow: str):
    # inflow should be of the form: "predict-0", "predict-1", ..., "predict-2499"
    prediction = app.model.predict(app.data.iloc[int(inflow.split("-")[1]), :].to_frame().T)[0]
    return {"prediction": app.dict[prediction]}


if __name__ == '__main__':
    app.run("localhost", port=5000)
