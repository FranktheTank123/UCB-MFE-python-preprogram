import numpy as np
import pandas as pd

from sklearn.preprocessing import MaxAbsScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline

from sklearn.linear_model import Ridge
from sklearn.ensemble import AdaBoostRegressor


class AddShp(BaseEstimator, TransformerMixin):
    def __init__(self, tokens):
        self.tokens = tokens
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X_ = X.copy()
        for token in self.tokens:
            X_[f"shp_{token}"] = X_[f"ret_{token}"] / X_[f"vol_{token}"]
            X_.loc[X[f"vol_{token}"]==0, f"shp_{token}"] = 0.0
        return X_
    

pipeline = Pipeline([
    ("addshp", AddShp(['BTC', 'ETH', 'USDT', 'SOL', 'ADA', 'DOT', 'AVAX', 'ATOM', 'CRV', 'AAVE', 'COMP'])),
    ("impute", SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0.0)),
    ("scale", MaxAbsScaler()),
    ("pca", PCA()),
    ("model", AdaBoostRegressor(Ridge(), random_state=0))
])