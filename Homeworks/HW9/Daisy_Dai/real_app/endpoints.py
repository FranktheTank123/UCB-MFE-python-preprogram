import pickle
import numpy as np

from flask import Flask
from model_training import preping_data



def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'rb'))
    # this is not the best way to do it
    # app.data = X
    return app


app = creat_app()




@app.route("/<np.ndarray:features>")
def predict_iris(features: np.ndarray):
    # the input should be a numpy array of 4 numbers
    iris_type = app.model.predict(features)[0]
    return {"iris_type": iris_type}


if __name__ == '__main__':
    app.run("localhost", port=5000)
