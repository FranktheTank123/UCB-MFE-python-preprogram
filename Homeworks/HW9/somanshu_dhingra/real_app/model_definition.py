from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import Ridge


import numpy as np
import pandas as pd


from sklearn.base import BaseEstimator, TransformerMixin
# from sklearn.pipeline import Pipeline
# from sklearn.compose import ColumnTransformer,TransformedTargetRegressor
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.linear_model import Ridge
# from sklearn.model_selection import cross_validate
# from sklearn.model_selection import TimeSeriesSplit
# from sklearn.metrics import mean_squared_error, make_scorer
# from sklearn.model_selection import learning_curve


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.columns]

class EMA_FeatureTransformer(BaseEstimator, TransformerMixin):
    def __init__(self,alpha = None):
        self.alpha = alpha
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        if self.alpha is not None:
            X_ = X.copy()
            X_ = pd.DataFrame(X_).ewm(alpha = self.alpha, ignore_na = True).mean().values
            return X_
        else:
            return X

        
pipeline = Pipeline([
    ('impute', SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0.)),
    ('EMA', EMA_FeatureTransformer()),
    ('scale', StandardScaler()),
    ('pca', PCA()),
    ('model', Ridge())
])




