import pickle

import click
import numpy as np
import pandas as pd
from model_definition import pipeline
from sklearn.model_selection import GridSearchCV


def prepare_data(data_location) -> tuple[pd.DataFrame, pd.Series, dict]:
    data = pd.read_excel(data_location)
    classes = data["Class"].unique()
    classes_dict = {0: classes[0], 1: classes[1]}
    data["Class"] = data["Class"].map({classes[0]: 0, classes[1]: 1})
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y, classes_dict


@click.command()
@click.option("--data-path")
@click.option("--model-path")
def main(data_path, model_path):
    X, y, _ = prepare_data(data_location=data_path)
    print(f"preparing data complete, X: {X.shape} y: {y.shape}")
    search = GridSearchCV(
        pipeline,
        {
            "pca__n_components": [1, 2, 3, 5, 6, 8, 10, 12],
            "model__C": np.arange(0.1, 1.1, 0.1),
        },
        scoring="accuracy",
        refit=True,
        cv=10,
        n_jobs=-1,
    )
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")
    pickle.dump(best_model, open(model_path, "wb"))


if __name__ == "__main__":
    main()
