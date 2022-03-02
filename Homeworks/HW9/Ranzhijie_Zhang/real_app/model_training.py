from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click
import sqlite3

%load_ext sql

from platform import python_version
from model_definition import pipeline





def preping_data(data_location):

    df = pd.read_csv('~/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Ranzhijie_Zhang/data/data.csv')
    y = df['price']
    X = df[2:]
    return X, y


@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.2
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    search = GridSearchCV(pipeline, {
        'pca__n_components': [1, 5, 10, 20, 22],
        'model__alpha': [0.1, 0.5, 1.]
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
   # data_path = "~/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Ranzhijie_Zhang/data/data.csv"
    # model_path = '~/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Ranzhijie_Zhang/data/trained_model.pckl'
    main(data_path,model_path)
