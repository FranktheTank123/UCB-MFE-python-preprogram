from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click


from model_definition import pipeline


def vol_ohlc(df, lookback=3):
    o = df.open
    h = df.high
    l = df.low
    c = df.close

    k = 0.34 / (1.34 + (lookback + 1) / (lookback - 1))
    cc = np.log(c / c.shift(1))
    ho = np.log(h / o)
    lo = np.log(l / o)
    co = np.log(c / o)
    oc = np.log(o / c.shift(1))
    oc_sq = oc ** 2
    cc_sq = cc ** 2
    rs = ho * (ho - co) + lo * (lo - co)
    close_vol = cc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    open_vol = oc_sq.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    window_rs = rs.rolling(lookback).sum() * (1.0 / (lookback - 1.0))
    result = (open_vol + k * close_vol + (1 - k) * window_rs).apply(np.sqrt) * np.sqrt(252)
    result[:lookback - 1] = np.nan

    return result


# this is just copying from Lecture 8's notebook
def preping_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    # this should be a global variable
    # data_location = 'sqlite:////Users/tianyixia/dev/UCB-MFE-python-preprogram/data/data.db'
    ohlc = pd.read_sql('SELECT * FROM ohlc', data_location)

    def df_merge(left, right):
        return pd.merge(left, right, on='ts', how='inner')

    tokens = ohlc.token.unique()
    X = reduce(df_merge, [
        (lambda df:
         (
             df
                 .assign(
                 vol=vol_ohlc(df).fillna(0),
                 ret=df.close.pct_change()
             )[['ts', 'vol', 'ret']]
                 .rename(columns={
                 col: f'{col}_{token}' for col in ['ts', 'vol', 'ret'] if col != 'ts'
             })
         ))(ohlc[ohlc.token == token])
        for token in tokens
    ]).set_index('ts')

    ETH_tokens = ohlc[ohlc['chain'] == 'ETH'].token.unique()

    ret_ETHs = list(map(lambda x: f"ret_{x}", ETH_tokens))
    vol_ETHs = list(map(lambda x: f"vol_{x}", ETH_tokens))

    X.fillna(0, inplace = True)

    pca = PCA(n_components=1)
    X['vol_ETHS'] = pca.fit_transform(X[vol_ETHs])
    X['ret_ETHS'] = pca.fit_transform(X[ret_ETHs])
    X.drop(ret_ETHs, axis=1, inplace=True)
    X.drop(vol_ETHs, axis=1, inplace=True)

    factors = set(list(map(lambda x: x[4:], X.columns)))
    for factor in factors:
        X[f'ret3_{factor}']= X[f'ret_{factor}'].rolling(3).sum()
        X[f'ret3/vol_{factor}']= X[f'ret3_{factor}']/X[f'vol_{factor}'] # this refers to the pseudo Sharpe-ratio

    y = X.ret_SOL.shift(-1)[10:-1]
    X = X[10:-1]        

    #y = X.ret_SOL.shift(-1)[:-1]
    #X = X[:-1]
    return X, y


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
        'pca__n_components': np.linspace(10,20,11).astype(int),
        'model__alpha': np.linspace(0,1,6)
    }, scoring=scorer, refit=True, cv=cv, verbose = 2)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
