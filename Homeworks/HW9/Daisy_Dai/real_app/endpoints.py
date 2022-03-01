import pickle
import numpy as np

from flask import Flask




def creat_app():
    app = Flask(__name__)
    app.model = pickle.load(open('C:/Users/15103/OneDrive/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Daisy_Dai/data/trained_model.pckl', 'rb'))
    
    return app


app = creat_app()




@app.route("/<np.ndarray:features>")
def predict_iris(features: np.ndarray):
    # the input should be a numpy array of 4 numbers
    y_pred = round(app.model.predict(features)[0])
    classification = ['setosa', 'versicolor', 'virginica']
    iris_type = classification[y_pred]
    return {"iris_type": iris_type}


if __name__ == '__main__':
    app.run("localhost", port=5000)
