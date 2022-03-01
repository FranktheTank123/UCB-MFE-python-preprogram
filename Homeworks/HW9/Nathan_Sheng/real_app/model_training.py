import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functools import reduce

import pickle

from model_definition import pipeline

data_location = 'sqlite:///../data/data.db'

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

ohlc = pd.read_sql('SELECT * FROM ohlc', data_location)

tokens = ohlc.token.unique()

def df_merge(left, right):
    return pd.merge(left, right, on='ts', how='inner')

def get_data():
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

    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
    return X, y

pipeline.fit(*get_data())
pickle.dump(pipeline, open("../data/model.pckl", "wb"))