# =============================================================================
# Homework 2
# 
# =============================================================================

import pandas as pd
import numpy as np
import requests

# =============================================================================
# Part 1. Getting the Crypto dataframe:
# =============================================================================

def get_data(token):
    if token != "FLOW":
        res = requests.get(
            f'https://api.cryptowat.ch/markets/coinbase-pro/{token}usd/ohlc',
            params={
                'periods': '3600',
                'after': str(int(pd.Timestamp('2021-11-22').timestamp()))
            }
        )
    else:
        res = requests.get(
            f'https://api.cryptowat.ch/markets/kraken/{token}usd/ohlc',
            params={
                'periods': '3600',
                'after': str(int(pd.Timestamp('2021-11-22').timestamp()))
            }
        )

    df = pd.DataFrame(
        res.json()['result']['3600'],
        columns=['ts', 'open', 'high', 'low', 'close', 'volume', 'volumeUSD']
    )
    df['ts'] = pd.to_datetime(df.ts, unit='s')
    df['token'] = token
    
    return df

tokens = ['ETH', 'SOL', 'AVAX', 'USDT', 'FLOW']

dfs = [
    (lambda x: x.assign(chain=x.token))(get_data(token)) 
    for token in tokens
    ]

df_base = pd.concat(get_data(token) for token in tokens)
df = df_base.set_index('ts')

# =============================================================================
# Part 2, sorting volume USD
# =============================================================================

df_USDvolume = df.groupby('token')['volumeUSD'].sum().to_frame()
df_USDvolume = df_USDvolume.sort_values('volumeUSD', ascending=False)

# =============================================================================
# Part 3, calculate close ETH/SOL
# =============================================================================

ETH_SOL_close_ratio=pd.merge(
                                dfs[0][['ts', 'close']].rename(columns={'close': f'close_{tokens[0]}'}),
                                dfs[1][['ts', 'close']].rename(columns={'close': f'close_{tokens[1]}'}),
                                on='ts',
                                how='inner'
                                )


ETH_SOL_close_ratio["ETH/SOL"] = ETH_SOL_close_ratio["close_ETH"]/ETH_SOL_close_ratio["close_SOL"]

# =============================================================================
# Part 4, change volume and volumeUSD name
# =============================================================================

df.rename(
    columns={
        'volume':'volumeBase',
        'volumeUSD':'volumeTerm'
    }
)

# =============================================================================
# Part 5, fat table 
# =============================================================================
import functools

dfs_close_base = (dfs[0][["ts","close"]].rename(columns={'close': f'close_{tokens[0]}'}), 
                  dfs[1][["ts","close"]].rename(columns={'close': f'close_{tokens[1]}'}),
                  dfs[2][["ts","close"]].rename(columns={'close': f'close_{tokens[2]}'}),
                  dfs[3][["ts","close"]].rename(columns={'close': f'close_{tokens[3]}'}),
                  dfs[4][["ts","close"]].rename(columns={'close': f'close_{tokens[4]}'}))

dfs_close = functools.reduce(lambda left,right: pd.merge(left,right,on='ts'), dfs_close_base)

dfs_close = dfs_close.set_index('ts')

# =============================================================================
# Part 6, hourly log return of each token
# =============================================================================

#Calculate the % return using pct_change then adjust the formula to calc. log return    
    
dfs_close[f'close_{tokens[0]}_logreturn'] = np.log(dfs_close[f'close_{tokens[0]}'].pct_change(1)+1)
dfs_close[f'close_{tokens[1]}_logreturn'] = np.log(dfs_close[f'close_{tokens[1]}'].pct_change(1)+1)
dfs_close[f'close_{tokens[2]}_logreturn'] = np.log(dfs_close[f'close_{tokens[2]}'].pct_change(1)+1)
dfs_close[f'close_{tokens[3]}_logreturn'] = np.log(dfs_close[f'close_{tokens[3]}'].pct_change(1)+1)
dfs_close[f'close_{tokens[4]}_logreturn'] = np.log(dfs_close[f'close_{tokens[4]}'].pct_change(1)+1)

# Now dfs_close has the log return column

# =============================================================================
# Part 7 & 8, Correlation and plot
# =============================================================================

Corr = dfs_close[[f'close_{tokens[0]}_logreturn', 
                           f'close_{tokens[1]}_logreturn', 
                           f'close_{tokens[2]}_logreturn', 
                           f'close_{tokens[3]}_logreturn', 
                           f'close_{tokens[4]}_logreturn']].corr(method='pearson')

#Print out the correlation matrix
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(Corr)

#Plotting out the correlation

import matplotlib.pyplot as plt

fig = plt.figure()
axis = fig.add_subplot(111)
fig.colorbar(axis.matshow(Corr))

axis.set_xticklabels(['']+tokens)
axis.set_yticklabels(['']+tokens)    
plt.show()
