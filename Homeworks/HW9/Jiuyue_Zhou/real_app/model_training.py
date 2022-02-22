import numpy as np
import pandas as pd
from functools import reduce
import pickle

import click

from sklearn.model_selection import TimeSeriesSplit, GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer

from model_definition import pipeline

data_location = "sqlite:///../data/data.db"


def vol_ohlc(df, lookback=10):
    o = df.open
    h = df.high
    l = df.low
    c = df.close
    
    k = 0.34 / (1.34 + (lookback+1)/(lookback-1))
    cc = np.log(c/c.shift(1))
    ho = np.log(h/o)
    lo = np.log(l/o)
    co = np.log(c/o)
    oc = np.log(o/c.shift(1))
    oc_sq = oc**2
    cc_sq = cc**2
    rs = ho*(ho-co)+lo*(lo-co)
    close_vol = cc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    open_vol = oc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    window_rs = rs.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    result = (open_vol + k * close_vol + (1-k) * window_rs).apply(np.sqrt) * np.sqrt(252)
    result[:lookback-1] = np.nan
    
    return result


def preping_data(data_location):
    ohlc = pd.read_sql("""
    SELECT  
    * 
    FROM
    ohlc
    """, data_location)
    
    def df_merge(left, right):
        return pd.merge(left, right, on="ts", how="inner")
    
    tokens = ohlc.token.unique()
    X = reduce(df_merge, [
               (lambda df: df.assign(vol=vol_ohlc(df).fillna(0),
                                    ret=df.close.pct_change()
                                   )[["ts","vol","ret"]].rename(
                                   columns={col: f"{col}_{token}" for col in ["vol", "ret"]}
                                   )
               )(ohlc[ohlc.token == token])
               for token in tokens]
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
    print(f"preping data complete, X: {X.shape}, y: {y.shape}")
    
    test_size = 0.2
    cv = TimeSeriesSplit(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = make_scorer(mean_squared_error, greater_is_better=False, squared=False)
    
    param_grid = {
        "pca__n_components": [1, 5, 10, 20, 33],
        "model__n_estimators": [25, 50, 75],
        "model__base_estimator__alpha": [0.1, 0.5, 1.0],
    }

    pipeline_cv = GridSearchCV(pipeline, param_grid, cv=cv, scoring=scorer, n_jobs=-1)
    pipeline_cv.fit(X, y)
    best_model = pipeline_cv.best_estimator_
    print(f"model training done. Best params: {pipeline_cv.best_params_}")
    
    # model_path = "../data/best_model.pkl"
    pickle.dump(best_model, open(model_path, "wb"))
    

if __name__ == "__main__":
    main()