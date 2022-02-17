import pandas as pd
import numpy as np
import talib
from functools import reduce
import pickle
import click

from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.model_selection import GridSearchCV

from model_definition import pipeline

data_location = 'sqlite:///../data/data.db'


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


def calculate_features(ohlc, token):
    df = ohlc[ohlc['token'] == token].copy()
    df['ret'] = df.close.pct_change()
    df['mfi'] = talib.MFI(df.high, df.low, df.close, df.volume, timeperiod=14) / 100
    df['mom_5'] = talib.MOM(df.close, timeperiod=5) / df.close
    df['mom_10'] = talib.MOM(df.close, timeperiod=10) / df.close
    df['ppo'] = talib.PPO(df.close, fastperiod=12, slowperiod=26, matype=0)
    df['rsi'] = talib.RSI(df.close, timeperiod=14) / 100
    df['obv'] = talib.OBV(df.close, df.volume) / df.volume
    df['obv'] = np.sign(df.obv) * np.log(df.obv.abs())
    df['vol'] = vol_ohlc(df).fillna(0)
    df['atr'] = talib.ATR(df.high, df.low, df.close, timeperiod=14) / df.close

    select_columns = ['ts', 'ret', 'mfi', 'mom_5', 'mom_10', 'ppo', 'rsi', 'obv', 'vol', 'atr']
    df = df[select_columns].rename(
        columns={col: f'{col}_{token}' for col in select_columns if col != 'ts'})
    return df



def preping_data(data_location):
    ohlc = pd.read_sql('SELECT * FROM ohlc', data_location)

    def df_merge(left, right):
        return pd.merge(left, right, on='ts', how='inner')

    tokens = ohlc.token.unique()
    X = reduce(df_merge, [calculate_features(ohlc, token) for token in tokens]).set_index('ts')
    X = X.fillna(0)
    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
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
        'model__n_estimators': [10, 30, 100],
        'model__max_depth': [3, 5, 8],
        'model__learning_rate': [0.01, 0.05, 0.1],
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)

    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")

    # model_path = '../data/best_model.pkl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
