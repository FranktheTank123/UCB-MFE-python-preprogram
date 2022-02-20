import pandas as pd
import numpy as np
from functools import reduce
import pickle
import click

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


# this is just copying from Lecture 8's notebook
def preping_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    ohlc = pd.read_sql('SELECT * FROM ohlc', data_location)
    tokens = ohlc.token.unique()
    def df_merge(left, right):
        return pd.merge(left, right, on='ts', how='inner')
    colNames = ['ts', 'vol', 'ret', 'voluPct', 'ret3', 'ret6', 'ret12', 'ret24', 'vol3', 'vol12', 'voluPct3']
    colNames = ['ts', 'vol', 'ret', 'voluPct', 'ret3', 'ret6', 'ret12', 'ret24', 'vol3', 'vol12', 'voluPct3']
    X = reduce(df_merge, [
        (lambda df: 
        (
            df.assign(
                vol = vol_ohlc(df).fillna(0),
                ret = df.close.pct_change(),
                voluPct = df.volumeUSD.pct_change(),
                ret3 = df.close.pct_change().rolling(3).mean(),
                ret6 = df.close.pct_change().rolling(6).mean(),
                ret12 = df.close.pct_change().rolling(6).mean(),
                ret24 = df.close.pct_change().rolling(24).mean(),
                vol3 = vol_ohlc(df).fillna(0).rolling(3).mean(),
                vol12 = vol_ohlc(df).fillna(0).rolling(12).mean(),
                voluPct3 = df.volumeUSD.pct_change().rolling(3).mean()
            )[colNames]
            .rename(columns={
                col: f'{col}_{token}' for col in colNames if col != 'ts'
            })
        ))(ohlc[ohlc.token == token])
        for token in tokens
    ]).set_index('ts')
    X = X.dropna()
    y = X.ret_SOL.shift(-1)[:-1]
    X = X[:-1]
    return X, y

# basically when you are calling this python program to train your model
# in the following example-ish format:
#(mfe-preprogram) PS C:\DAHOU\Education\UCBerkeleyMFE\PrepList\PreProgramCourse
#s\Python\UCB-MFE-python-preprogram\Homeworks\HW9\DAHOU_ZHENG\real_app> python 
#model_training.py --data-path sqlite:///C:/DAHOU/Education/UCBerkeleyMFE/PrepL
#ist/PreProgramCourses/Python/UCB-MFE-python-preprogram/Homeworks/HW9/DAHOU_ZHE
#NG/data/data.db  --model-path C:/DAHOU/Education/UCBerkeley/PrepList/PreProgra
#mCourses/Python/UCB-MFE-python-preprogram/Homeworks/HW9/DAHOU_ZHENG/data/train
#ed_model.pckl



@click.command()
@click.option('--data-path')
@click.option('--model-path')
def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    best_model = pipeline.fit(X,y)
    print(f"model training done. Best params: {best_model.get_params}")

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
