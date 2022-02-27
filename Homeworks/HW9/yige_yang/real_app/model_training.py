from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
import pandas as pd
import numpy as np
from functools import reduce
import pickle


from model_definition import pipeline


def vol_ohlc(df, lookback=10):
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


def preping_data():
    ohlc = pd.read_sql('SELECT * FROM ohlc', 'sqlite:///data.db')

    def df_merge(left, right):
        return pd.merge(left, right, on='ts', how='inner')

    tokens = ohlc.token.unique()
    X = reduce(df_merge, [
        (lambda df:
         (
             df
                 .assign(
                 vol=vol_ohlc(df),
                 ret=(df.high-df.low)/df.close
             )[['ts', 'vol', 'ret']]
                 .rename(columns={
                 col: f'{col}_{token}' for col in ['ts', 'vol', 'ret'] if col != 'ts'
             })
         ))(ohlc[ohlc.token == token])
        for token in tokens
    ]).set_index('ts').dropna(axis=0)
    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
    return X, y



def main():
    X, y = preping_data()
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

    pickle.dump(best_model, open('C:/Users/15840/Desktop/MFE_Python_Preprogram/Assignment8/best_model.pkl', 'wb'))


if __name__ == '__main__':
    main()

    