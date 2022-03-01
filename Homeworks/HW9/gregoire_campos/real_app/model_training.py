import pickle
from functools import reduce

import click
import numpy as np
import pandas as pd
from sklearn.metrics import make_scorer, mean_squared_error
from sklearn.model_selection import GridSearchCV, TimeSeriesSplit

from model_definition import pipeline


def vol_ohlc(df, lookback=10):
    o = df.open
    h = df.high
    low = df.low
    c = df.close

    k = 0.34 / (1.34 + (lookback + 1) / (lookback - 1))
    cc = np.log(c / c.shift(1))
    ho = np.log(h / o)
    lo = np.log(low / o)
    co = np.log(c / o)
    oc = np.log(o / c.shift(1))
    oc_sq = oc ** 2
    cc_sq = cc ** 2
    rs = ho * (ho - co) + lo * (lo - co)
    close_vol = cc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    open_vol = oc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    window_rs = rs.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    result = open_vol + k * close_vol + (1 - k) * window_rs
    result = result.apply(np.sqrt) * np.sqrt(252)
    result[: lookback - 1] = np.nan
    return result


def df_merge(left, right):
    return pd.merge(left, right, on="ts", how="inner")


def preping_data(data_location):
    # I didn't change anything here.
    ohlc = pd.read_sql("SELECT * FROM ohlc", data_location)
    tokens = ohlc.token.unique()
    X = reduce(
        df_merge,
        [
            (
                lambda df: (
                    df.assign(vol=vol_ohlc(df).fillna(0), ret=df.close.pct_change())[
                        ["ts", "vol", "ret"]
                    ].rename(
                        columns={
                            col: f"{col}_{token}"
                            for col in ["ts", "vol", "ret"]
                            if col != "ts"
                        }
                    )
                )
            )(ohlc[ohlc.token == token])
            for token in tokens
        ],
    ).set_index("ts")
    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
    return X, y


@click.command()
@click.option("--data-path")
@click.option("--model-path")
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.2
    # We kept the 80-20 proportions proposed
    # Here, we just added some pca_n_components and alpha to try.
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)

    search = GridSearchCV(
        pipeline,
        {
            "pca__n_components": [1, 5, 10, 15, 20, 22],
            "model__alpha": [0.1, 0.5, 1.0, 2.0],
        },
        scoring=scorer,
        refit=True,
        cv=cv,
        n_jobs=-1,
    )
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")
    pickle.dump(best_model, open(model_path, "wb"))


if __name__ == "__main__":
    main()
