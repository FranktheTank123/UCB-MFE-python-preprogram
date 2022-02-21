import pickle
import os
import sys

from flask import Flask

root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir + '/real_app')

from model_training import preping_data

def creat_app():
    app = Flask(__name__)
    root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
    app.model = pickle.load(open(os.path.join(root_dir, 'data', 'trained_model.pckl'), 'rb'))
    # "/Volumes/GoogleDrive-117908276173395970180/My Drive/UCB MFE Preprograms/Python/UCB MFE python/Homeworks/HW9/Yongjin_Kim/data/trained_model.pckl"
    app.data, _ = preping_data('sqlite:///' + root_dir + '/data/data.db')
    # "sqlite:////Volumes/GoogleDrive-117908276173395970180/My Drive/UCB MFE Preprograms/Python/UCB MFE python/Homeworks/HW9/Yongjin_Kim/data/data.db"
    return app


app = creat_app()


@app.route("/")
def HW9():
    return "<p>HW9 Milestone project</p>"


@app.route("/<string:time_stamp>")
def predict_rel_sol(time_stamp: str):
    # time stamp should be of the form: "2021-12-01 00:00:00"
    # my data starts from "2021-11-01 10:00:00" 
    ret_sol = app.model.predict(
        app.data.loc[time_stamp.replace("_"," ")].to_frame().T
    )[0]
    return {"ret_sol": ret_sol}


if __name__ == '__main__':
    app.run("localhost", port=5005)
