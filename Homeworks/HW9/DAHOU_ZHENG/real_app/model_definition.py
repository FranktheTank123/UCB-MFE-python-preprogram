from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Ridge

pipeline = Pipeline([
    ('pca', PCA(n_components=10)),
    ('model', Ridge(alpha=1.))
])



