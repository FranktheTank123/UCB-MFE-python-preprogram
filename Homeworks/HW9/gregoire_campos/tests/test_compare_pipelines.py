import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def evaluate_model(model, X, y, test_size=0.2):
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)
    return np.mean(
        cross_validate(model, X, y, cv=cv, scoring=scorer, n_jobs=-1)["test_score"]
    )


pipeline = Pipeline(
    [
        (
            "impute",
            SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0.0),
        ),
        ("scale", StandardScaler()),
        ("model", RandomForestRegressor(n_estimators=100, random_state=0)),
    ]
)
X = pd.read_csv("X.csv", index_col=0)
y = pd.read_csv("y.csv", index_col=0)


def test():
    assert (evaluate_model(pipeline, X, y)) > -0.010
    assert (evaluate_model(pipeline, X, y)) < -0.007
