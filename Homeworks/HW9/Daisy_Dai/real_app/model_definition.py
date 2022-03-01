from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline



pipeline = Pipeline([
    ('knn', KNeighborsClassifier())
])