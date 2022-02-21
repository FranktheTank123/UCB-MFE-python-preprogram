import numpy as np
import pandas as pd
import pickle
import click

from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from sklearn.metrics import make_scorer

from model_definition import pipeline

def preping_data(data_path):
    df = pd.read_csv(data_path) # The default data comes from kaggle-ubiquant sub-data
    df.set_index("time_id", inplace=True)
    y = df.pop("target")
    features = [f'f_{i}' for i in range(300)]
    X = df[features]
    return X, y

@click.command()
@click.option("--data-path", default="../data/data.csv")
@click.option("--model-path", default="../data/base_model.pkl")
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

    X, y = preping_data(data_path=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    cv = TimeSeriesSplit(n_splits=10)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=True)
    search = GridSearchCV(pipeline, {
        'model__num_leaves': [16, 32, 64],
        'model__learning_rate': [0.1, 0.5, 1],
        'model__n_estimators': [50, 100, 500]
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    pickle.dump(best_model, open(model_path, "wb"))

if __name__ == "__main__":
    main()