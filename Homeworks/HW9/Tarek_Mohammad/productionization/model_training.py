from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click

P = PCA
SI = SimpleImputer
RI = Ridge
MSE = mean_squared_error
MS = make_scorer
TSS = TimeSeriesSplit
GS = GridSearchCV

from sklearn.pipeline import Pipeline

data_location = 'sqlite:///data/data.db'


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
    rs = ho*(ho-co)+lo*(lo-co)
    cc_sq = cc**2
    close_vol = cc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    open_vol = oc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    window_rs = rs.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    result = (open_vol + k * close_vol + (1-k) * window_rs).apply(np.sqrt) * np.sqrt(252)
    result[:lookback-1] = np.nan
    
    return result




def preping_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    
    ohlc = pd.read_sql('SELECT * FROM ohlc', data_location)
    
    high_low = ohlc['high'] - ohlc['low']
    high_cp = np.abs(ohlc['high'] - ohlc['close'].shift())
    low_cp = np.abs(ohlc['low'] - ohlc['close'].shift())

    df = pd.concat([high_low, high_cp, low_cp], axis=1)
    true_range = np.max(ohlc, axis=1)

    def df_merge(left, right):
        return pd.merge(left, right, on='ts', how='inner')

    tokens = ohlc.token.unique()
    X = reduce(df_merge, [
        (lambda df: 
        (
            df
                .assign(
                vol=vol_ohlc(df).fillna(0),
                ret=df.close.pct_change(),
                ret_period_2 = df.close.pct_change(2).fillna(0),
                volume_price_trend = (df.close.pct_change()*df.volume).fillna(0),
                USD_vol_ret = df.volumeUSD.pct_change().fillna(0),
                average_true_range = true_range.rolling(14).mean().fillna(0)
            )[['ts', 'vol', 'ret', 'ret_period_2', 'volume_price_trend', 'USD_vol_ret', 'average_true_range']]
                .rename(columns={
                col: f'{col}_{token}' for col in ['ts', 'vol', 'ret', 'ret_period_2', 'volume_price_trend', 'USD_vol_ret', 'average_true_range'] if col != 'ts'
            })
        ))(ohlc[ohlc.token == token])
        for token in tokens
    ]).set_index('ts')
    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
    return X, y


@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):
    assert data_path and model_path, "invalid path"

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.2
    cv = TSS(n_splits=int(y.shape[0] * test_size), test_size=1)
    scorer = MS(MSE, greater_is_better=False, squared=False)

    search = GS(Pipeline, {
        'pca__n_components': [5, 10, 20, 40, 66],
        'model__alpha': [0.1, 0.5]
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
