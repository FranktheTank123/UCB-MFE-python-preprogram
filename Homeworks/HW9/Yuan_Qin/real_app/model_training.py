from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click


from model_definition import pipeline


def preping_data() :
    # this should be a global variable
    # data_location = 'sqlite:////Users/tianyixia/dev/UCB-MFE-python-preprogram/data/data.db'
    from sklearn.datasets import load_iris
    data = load_iris()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(df[data.feature_names], df['target'], random_state=0)
    return X_train, X_test, Y_train, Y_test


@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

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

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
