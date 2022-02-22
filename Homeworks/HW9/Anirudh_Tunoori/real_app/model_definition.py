from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import Ridge


pipeline = Pipeline([
		("scale", StandardScaler()),
		("pca", PCA()),
		("model", Ridge())
])
