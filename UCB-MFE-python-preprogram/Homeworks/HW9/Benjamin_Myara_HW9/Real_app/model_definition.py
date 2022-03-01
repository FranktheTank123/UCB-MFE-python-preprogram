import numpy as np
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipeline = Pipeline(
    [
        (
            "impute",
            SimpleImputer(missing_values=np.nan, strategy="constant", fill_value=0.0),
        ),
        ("scale", StandardScaler()),
        ("pca", PCA()),
        ("model", Ridge()),
    ]
)