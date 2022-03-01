from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC


import numpy as np

pipeline = Pipeline([
    ('scale', StandardScaler()),
    ('pca', PCA()),
    ('model', SVC())
])





