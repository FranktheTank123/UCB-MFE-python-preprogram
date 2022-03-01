from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import numpy as np
import pickle
import click


from model_definition import pipeline


def prep_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    df = pd.read_csv(data_location).set_index('Date')
    df['UL-RF'] = df.UN - df.RF
    df['MKT-RF'] = df.MKT - df.RF
    df['PG-RF'] = df.PG - df.RF
    df['HH-RF'] = df.HH-df.RF
    df['const'] = 1
    y = df['UL-RF']
    X = df[['const','MKT-RF','HH-RF','PG-RF']]
    
    return X, y


@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"
    X, y = prep_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.2
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    search = GridSearchCV(pipeline, {
        'EMA__alpha': [0.1,0.2,0.5,0.7,1.0],
        'pca__n_components': [1, 2, 3, 4],
        'model__alpha': [0.1, 0.5, 1.0]
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
