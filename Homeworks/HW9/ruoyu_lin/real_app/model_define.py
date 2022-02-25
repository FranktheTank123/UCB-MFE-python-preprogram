from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

from sklearn.pipeline import Pipeline

from xgboost import XGBRegressor
import numpy as np

pipeline = Pipeline([
    ('impute', SimpleImputer(missing_values=np.nan, strategy='constant', fill_value=0.)),
    ('scale', StandardScaler()),
    ("model", XGBRegressor(n_estimators = 100, 
                             objective = "reg:squarederror", 
                             n_jobs = -1,
#                              verbose = 0
                            ))
])