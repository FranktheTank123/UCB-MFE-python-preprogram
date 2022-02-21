from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline

from sklearn.linear_model import Ridge
import numpy as np

class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns
        
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.columns]



fac1, fac2, fac3, fac4, fac5 = 'AVAX', 'ADA', 'BTC', 'ATOM', 'USDT'

pipeline = Pipeline([
    ('feature_selector', FeatureSelector([f'ret_{fac1}',f'ret3_{fac1}',f'ret3/vol_{fac1}',f'vol_{fac1}',
                                          f'ret_{fac2}',f'ret3_{fac2}',f'ret3/vol_{fac2}',f'vol_{fac2}',
                                          f'ret_{fac3}',f'ret3_{fac3}',f'ret3/vol_{fac3}',f'vol_{fac3}',
                                          f'ret_{fac4}',f'ret3_{fac4}',f'ret3/vol_{fac4}',f'vol_{fac4}',
                                          f'ret_{fac5}',f'ret3_{fac5}',f'ret3/vol_{fac5}',f'vol_{fac5}'])),
    ('scale', StandardScaler()),
    ('pca', PCA()),
    ('model', Ridge())
])





