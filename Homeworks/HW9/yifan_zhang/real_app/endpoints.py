import pickle
from flask import Flask
from model_training import preping_data

def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open(
        'D:/Yifan/Berkeley/pre-course/python/UCB-MFE-python-preprogram/Homeworks/HW9/yifan_zhang/data/best_model.pkl',
        'rb'))
    app.data, _ = preping_data(
        'sqlite:///D:/Yifan/Berkeley/pre-course/python/UCB-MFE-python-preprogram/Homeworks/HW9/yifan_zhang/data/data.db')
    return app


app = creat_app()


@app.route("/")
def welcome_page():
    return "<p>Welcome to use the SOL hourly return prediction model!</p>"


@app.route("/<string:time_stamp>")
def predict(time_stamp: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    """
    predict SOL hourly return
    """
    ret_sol = app.model.predict(
        app.data.loc[time_stamp].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5000)
