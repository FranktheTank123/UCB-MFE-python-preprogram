from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


pipeline = Pipeline([
    ('scale', StandardScaler()),
    ('pca', PCA()),
    ('model', LogisticRegression(penalty="l2"))
])
