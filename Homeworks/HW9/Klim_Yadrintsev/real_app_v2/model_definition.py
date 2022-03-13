from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import Ridge


import numpy as np

pipeline = Pipeline([
    ('model', RandomForestRegressor(n_estimators=100, random_state=0, verbose=1))
])





