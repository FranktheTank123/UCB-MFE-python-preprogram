import numpy as np
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline

# Model highlighted by our study in compare_pipelines.py

pipeline = Pipeline(
    [
        (
            "impute",
            SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0.0),
        ),
        ("pca", PCA()),
        ("model", Lasso()),
    ]
)
