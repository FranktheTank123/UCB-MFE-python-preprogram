import pickle
from flask import Flask
from model_training import preping_data


def create_app():
    app = Flask(__name__)
    app.model = pickle.load(open("D:/UCB MFE/Preprogram Courses/Python/UCB-MFE-python-preprogram/Homeworks/HW9/Jiuyue_Zhou/data/best_model.pkl", "rb"))
    app.data, _ = preping_data("sqlite:///D:/UCB MFE/Preprogram Courses/Python/UCB-MFE-python-preprogram/Homeworks/HW9/Jiuyue_Zhou/data/data.db")
    return app


app = create_app()


@app.route("/")
def welcome():
    return "<p>Welcome to the SOL return prediction page!</p>"


@app.route("/<string:time_stamp>")
def predict_ret_sol(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    ret_sol = app.model.predict(app.data.loc[time_stamp].to_frame().T)[0]
    return {"ret_sol": ret_sol}


if __name__ == "__main__":
    app.run("localhost", port=5000)