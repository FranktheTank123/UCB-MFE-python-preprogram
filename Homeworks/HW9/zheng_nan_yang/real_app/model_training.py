from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click


from model_definition import pipeline


def preping_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    # this should be a global variable
    # data_location = 
    df = pd.read_csv(data_location)

    df["good"] = [1 if x >= 6 else 0 for x in df.quality]

    X = df[df.columns.drop(['quality','good'])]
    y = df['good']

    return X, y


@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

    search = GridSearchCV(pipeline, {
        'pca__n_components': [1, 2, 5, 8, 10],
        'model__C': [0.1, 1, 10, 100],
        'model__kernel': ['linear', 'rbf']
    }, refit=True, n_jobs=-1)
    search.fit(X_train, y_train)
    
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
