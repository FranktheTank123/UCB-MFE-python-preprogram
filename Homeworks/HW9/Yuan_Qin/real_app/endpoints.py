

from flask import Flask
from model_training import preping_data
import joblib

def creat_app():
    app = Flask(__name__)
    app.model =joblib.load('/Users/qinyuan/MFE2022Python/Homeworks/HW1/Yuan_QIN/UCB-MFE-python-preprogram/Homeworks/HW9/Yuan_Qin/Data/clf.pkl')
    # this is not the best way to do it
    # app.data = X
    app.X_train, app.X_test, app.Y_train, app.Y_test = preping_data()
    app.len=len(app.Y_train)
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # 
    time_stamp=int(time_stamp)%app.len
    ret_sol = app.model.predict(
        app.X_test.iloc[time_stamp:time_stamp+1]
    )[0]
    return {"ret_sol": str(ret_sol)}


if __name__ == '__main__':
    app.run("localhost", port=5000)
