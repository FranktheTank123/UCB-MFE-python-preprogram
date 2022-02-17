from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline
from lightgbm import LGBMRegressor


import numpy as np

pipeline = Pipeline(
    steps=[('impute', SimpleImputer(fill_value=0.0, strategy='constant')),
            ('model', LGBMRegressor(colsample_bytree=0.7, learning_rate=0.05, max_depth=5, n_estimators=30))]
)





