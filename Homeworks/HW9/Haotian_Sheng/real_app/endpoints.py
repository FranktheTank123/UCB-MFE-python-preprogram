import numpy as np 
from flask import Flask
from model_training import preping_data
import xgboost as xgb

def creat_app():
    data_path = 'D:/pre-program/python/hw9/UCB-MFE-python-preprogram/Homeworks/HW9/Haotian_Sheng/data/data.csv'
    model_path = 'D:/pre-program/python/hw9/UCB-MFE-python-preprogram/Homeworks/HW9/Haotian_Sheng/data/xgb.json'
    app = Flask(__name__)
    regr = xgb.XGBRegressor()
    regr.load_model(model_path)
    app.model = regr
    app.data, _ = preping_data(data_path)
    return app


app = creat_app()


@app.route("/")
def welcome_page():
    return "<p>Welcome to look at the houce prices prediction.</p>"


@app.route("/<int:id_number>")
def predict_house_price(id_number: str):
    house_prc = app.model.predict(app.data[app.data.index == int(id_number)])[0]
    house_prc = np.around(house_prc, 4)
    return {"house_price": str(house_prc)}


if __name__ == '__main__':
    app.run("localhost", port=5000)
