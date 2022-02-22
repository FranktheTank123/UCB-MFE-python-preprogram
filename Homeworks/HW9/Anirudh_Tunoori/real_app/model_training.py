import pickle

import click
import numpy as np
import pandas as pd
from model_definition import pipeline
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import (GridSearchCV, TimeSeriesSplit,
                                     cross_validate)


def load_data(data_location) -> pd.DataFrame:
    # data_location = '/data/chess_games_stats.csv'
    raw_data = pd.read_csv(data_location)
    raw_data = raw_data.set_index("Game ID")

    return raw_data


def evaluate_model(model, X, y, test_size=0.3):
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    return np.mean(
        cross_validate(model, X, y, cv=cv, scoring=scorer, n_jobs=-1)["test_score"]
    )


@click.command()
@click.option("--data-path")
@click.option("--model-path")
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

    train_data = load_data(data_location=data_path)
    train_data["rating_diff"] = train_data["White Rating"] - train_data["Black Rating"]
    X = train_data[
        [
            "rating_diff",
            "White Centi-pawn Loss",
            "White's Number of Inaccuracies",
            "White's Number of Mistakes",
            "White's Number of Blunders",
        ]
    ]
    y = train_data[["Black Centi-pawn Loss"]]
    print(f"Preparing data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.3
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    n_components = list(range(1, X.shape[1] + 1, 1))
    parameters = dict(pca__n_components=n_components, model__alpha=[0.1, 0.5, 1.0])
    search = GridSearchCV(
        pipeline, parameters, scoring=scorer, refit=True, cv=cv, n_jobs=-1
    )

    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"Model training complete. Best params: {search.best_params_}")
    evaluate_model(best_model, X, y)
    pickle.dump(best_model, open(model_path, "wb"))


if __name__ == "__main__":
    main()
