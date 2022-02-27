import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce
import pickle

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import QuantileTransformer
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.svm import SVR
from sklearn.model_selection import learning_curve

import numpy as np

pipeline = Pipeline([
    ('scale', QuantileTransformer(random_state=0, n_quantiles=5)),
    ('impute', SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0.)),
    ('model', RandomForestRegressor(max_depth=3,random_state=0))
])





