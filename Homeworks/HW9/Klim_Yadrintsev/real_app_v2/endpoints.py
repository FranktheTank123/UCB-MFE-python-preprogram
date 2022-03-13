import pickle
import pandas as pd

from flask import Flask


def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Volumes/ExtremePro/Coding/pre-program/python-pre/UCB-MFE-python-preprogram/Homeworks/HW9/Klim_Yadrintsev/data/best_model_students.pkl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    data_location = 'sqlite:///../data_v2/avocado.db'
    data = pd.read_sql('SELECT * FROM avocado', data_location)
    data = data.iloc[:, 1:]
    y = data.AveragePrice
    data.drop(['AveragePrice'], axis=1, inplace=True)
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

