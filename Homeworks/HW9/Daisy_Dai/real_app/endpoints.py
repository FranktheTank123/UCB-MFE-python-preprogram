import pickle
import numpy as np

from flask import Flask




def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('C:/Users/15103/OneDrive/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Daisy_Dai/data/trained_model.pckl', 'rb'))
    
    return app


app = creat_app()




@app.route("/<string:features>")
def predict_iris(features: str):
    # the input should be a string composed of four numbers
    # i.e. '3 4 5 6'
    x = np.fromstring(features, dtype=float, sep=' ').reshape(1,-1)
    y_pred = round(app.model.predict(x)[0])
    classification = ['setosa', 'versicolor', 'virginica']
    iris_type = classification[y_pred]
    return {"iris_type": iris_type}


if __name__ == '__main__':
    app.run("localhost", port=5000)
