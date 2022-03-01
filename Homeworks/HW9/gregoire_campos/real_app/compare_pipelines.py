import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import TimeSeriesSplit, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor

# This serves as a justification for the parameters we chose
from model_training import preping_data


def evaluate_model(model, X, y, test_size=0.2):
    data_path = "sqlite:////Users/campo/Desktop/MFEpython/Homeworks/HW9/gregoire_campos/data/data.db"
    X, y = preping_data(data_location=data_path)

    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)
    return np.mean(
        cross_validate(model, X, y, cv=cv, scoring=scorer, n_jobs=-1)["test_score"]
    )


def compare_models():
    data_path = "sqlite:////Users/campo/Desktop/MFEpython/Homeworks/HW9/gregoire_campos/data/data.db"
    X, y = preping_data(data_location=data_path)
    Dic_perf = {}

    pipeline = Pipeline(
        [
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("model", DecisionTreeRegressor(random_state=0)),
        ]
    )

    Dic_perf["Decision Tree"] = evaluate_model(pipeline, X, y)

    class FeatureSelector(BaseEstimator, TransformerMixin):
        def __init__(self, columns):
            self.columns = columns

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            return X[self.columns]

    pipeline = Pipeline(
        [
            ("feature_selector", FeatureSelector(["ret_SOL"])),
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("scale", StandardScaler()),
            ("model", RandomForestRegressor(n_estimators=100, random_state=0)),
        ]
    )

    Dic_perf["Random Forest regressor with feature selector"] = evaluate_model(
        pipeline, X, y
    )

    pipeline = Pipeline(
        [
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("scale", StandardScaler()),
            ("model", RandomForestRegressor(n_estimators=100, random_state=0)),
        ]
    )

    Dic_perf["Random Forest regressor"] = evaluate_model(pipeline, X, y)

    pipeline = Pipeline(
        [
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("scale", StandardScaler()),
            ("pca", PCA(n_components=5)),
            ("model", RandomForestRegressor(n_estimators=100, random_state=0)),
        ]
    )

    Dic_perf["Random Forest regressor PCA 5 components"] = evaluate_model(
        pipeline, X, y
    )

    pipeline = Pipeline(
        [
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("pca", PCA(n_components=20)),
            ("model", Ridge(alpha=1.0)),
        ]
    )

    Dic_perf["Ridge PCA 20"] = evaluate_model(pipeline, X, y)

    pipeline = Pipeline(
        [
            (
                "impute",
                SimpleImputer(
                    missing_values=np.nan, strategy="constant", fill_value=0.0
                ),
            ),
            ("pca", PCA(n_components=20)),
            ("model", Lasso(alpha=1.0)),
        ]
    )

    Dic_perf["Lasso PCA 20"] = evaluate_model(pipeline, X, y)

    return Dic_perf
    # Thus, we chose to focus on a Lasso model


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
