# HW2
Please do the following in a jupyter notebook:
- Get the time series for the following cryptocurrencies from `cryptowat.ch` starting from 2021-11-22, hourly data
    1. ETH
    2. SOL
    3. AVAX
    4. USDT
    5. FLOW
- Get the total USD volume traded for each token in a dataframe, sorted from highest volume to lowest volume
- Add a column that calculates the close price ratio between ETH and SOL for each house (i.e. close price of ETH / close price of SOL for each period)
- Change the name of the `volume` and `volumeUSD` columns to `volumeBase` and `volumeTerm`
- create a fat table indexed by the timestamp, and each column is the close price of each token (i.e. this should be a table of  200 rows and 5 columns)
- calculate the hour by hour log return of the close price of each token (return is calculated by np.log(price_t / price_{t-1}))
- \[Stretch\] calculate the correlation of the tokens using the table above
- \[Stretch\] visualize the correlation in a matplpotlib plot