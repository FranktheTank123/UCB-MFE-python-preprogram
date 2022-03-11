import pickle
import pandas as pd

from flask import Flask


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Volumes/ExtremePro/Coding/pre-program/python-pre/UCB-MFE-python-preprogram/Homeworks/HW9/Klim_Yadrintsev/data/best_model_students.pkl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    app.data = pd.read_csv('/Volumes/ExtremePro/Coding/pre-program/python-pre/UCB-MFE-python-preprogram/Homeworks/HW9/Klim_Yadrintsev/data/student_prediction.csv')
    app.data = app.data.drop('STUDENTID', axis=1)
    return app


app = creat_app()


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health_check")
def ping():
    return "pong"


@app.route("/<string:student_id>")
def predict_rel_student(student_id: str):
    # time stamp should be of the form: "2021-11-01 00:00:00"
    grade = app.model.predict(
        app.data.iloc[int(student_id)].to_frame().T
    )[0]
    return {"grade": int(grade)}


if __name__ == '__main__':
    app.run("localhost", port=5000)
