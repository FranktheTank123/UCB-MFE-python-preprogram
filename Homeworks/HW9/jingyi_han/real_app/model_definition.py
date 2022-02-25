import pickle
import os
import sys

import numpy as np
from skimage.io import imread
from skimage.transform import resize

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)

loaded_model = pickle.load(open(parent+"/data/model.pkl", "rb"))

labels = ["cat", "dog", "fox", "leopard", "tiger", "wolf", "cheetah", "lion"]


def data_process(path):
    img = imread(path)
    X = resize(img, (15, 15, 3)).flatten()
    X = X.reshape(1, len(X))
    return X


def mdl_predict(img_path):
    x = data_process(img_path)
    prob = loaded_model.predict_proba(x)
    pred_animal = labels[np.argmax(prob)]
    prob = [round(100 * prob[0][i], 2) for i in range(len(prob[0]))]
    return prob, pred_animal
