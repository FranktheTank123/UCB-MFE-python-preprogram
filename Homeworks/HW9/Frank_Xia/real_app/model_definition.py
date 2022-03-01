from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import Ridge


import numpy as np

pipeline = Pipeline([
    ('impute', SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0.)),
    ('scale', StandardScaler()),
    ('pca', PCA()),
    ('model', Ridge())
])

import pickle
from flask import Flask
app = Flask(__name__)
app.model = pickle.load(open('/Users/campo/Desktop/MFEpython/Homeworks/HW9/Frank_Xia/data/trained_model.pckl', 'rb'))
print (app.model)



