from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from lightgbm import LGBMRegressor

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ('model', LGBMRegressor(
        num_leaves=16,
        n_estimators=50,
        learning_rate=0.1
    ))
])