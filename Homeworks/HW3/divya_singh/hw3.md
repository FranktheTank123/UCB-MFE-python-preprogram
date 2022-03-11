importing packages


```python
import pandas as pd,numpy as np, os
import matplotlib.pyplot as plt
```

reading dataframe from csv


```python
#os.chdir("~/Documents/MFE_PREPROGRAMS/python/Homeworks/UCB-MFE-python-preprogram/Lectures/Lecture 3/data")
data = pd.read_csv("../../../Lectures/Lecture 3/data/hw3.csv")
data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ts</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>volumeUSD</th>
      <th>token</th>
      <th>chain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-12-02 14:00:00</td>
      <td>22.4150</td>
      <td>22.4913</td>
      <td>22.0816</td>
      <td>22.3516</td>
      <td>3.150215e+04</td>
      <td>NaN</td>
      <td>UNI</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-12-02 23:00:00</td>
      <td>4.8043</td>
      <td>4.8043</td>
      <td>4.7426</td>
      <td>4.7806</td>
      <td>7.368623e+04</td>
      <td>NaN</td>
      <td>CRV</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-12-10 15:00:00</td>
      <td>182.4900</td>
      <td>NaN</td>
      <td>175.2100</td>
      <td>175.8600</td>
      <td>7.373675e+04</td>
      <td>NaN</td>
      <td>SOL</td>
      <td>SOL</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-12-10 18:00:00</td>
      <td>3978.4300</td>
      <td>3989.7400</td>
      <td>3932.0000</td>
      <td>3972.3400</td>
      <td>1.850804e+04</td>
      <td>NaN</td>
      <td>ETH</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-12-08 21:00:00</td>
      <td>193.3240</td>
      <td>194.2420</td>
      <td>192.5640</td>
      <td>193.1540</td>
      <td>6.942691e+04</td>
      <td>NaN</td>
      <td>SOL</td>
      <td>SOL</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2021-12-08 12:00:00</td>
      <td>3.8405</td>
      <td>3.8789</td>
      <td>3.7900</td>
      <td>3.8392</td>
      <td>3.788895e+05</td>
      <td>NaN</td>
      <td>CRV</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2021-12-04 07:00:00</td>
      <td>188.6880</td>
      <td>196.4860</td>
      <td>185.2630</td>
      <td>190.8720</td>
      <td>1.041406e+04</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2021-12-05 02:00:00</td>
      <td>1.0015</td>
      <td>1.0016</td>
      <td>1.0012</td>
      <td>1.0013</td>
      <td>3.398077e+06</td>
      <td>NaN</td>
      <td>USDT</td>
      <td>USDT</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2021-12-09 10:00:00</td>
      <td>1.0009</td>
      <td>1.0010</td>
      <td>1.0008</td>
      <td>1.0009</td>
      <td>7.236563e+06</td>
      <td>NaN</td>
      <td>USDT</td>
      <td>USDT</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021-12-03 23:00:00</td>
      <td>20.0490</td>
      <td>20.1703</td>
      <td>19.9061</td>
      <td>19.9120</td>
      <td>3.884822e+04</td>
      <td>NaN</td>
      <td>UNI</td>
      <td>ETH</td>
    </tr>
  </tbody>
</table>
</div>



since dataset is notsorted by date and time, sorting data for better visualisation


```python
data.sort_values('ts', inplace=True)
data= data.reset_index(drop=True)
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ts</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>volumeUSD</th>
      <th>token</th>
      <th>chain</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-12-01 00:00:00</td>
      <td>210.3120</td>
      <td>NaN</td>
      <td>208.4320</td>
      <td>208.6760</td>
      <td>70031.618000</td>
      <td>NaN</td>
      <td>SOL</td>
      <td>SOL</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-12-01 00:00:00</td>
      <td>280.5900</td>
      <td>281.4000</td>
      <td>278.3000</td>
      <td>278.7000</td>
      <td>207.849000</td>
      <td>NaN</td>
      <td>COMP</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-12-01 00:00:00</td>
      <td>257.1020</td>
      <td>260.7750</td>
      <td>255.3450</td>
      <td>257.0780</td>
      <td>2730.299000</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-12-01 00:00:00</td>
      <td>21.2004</td>
      <td>21.3115</td>
      <td>21.0337</td>
      <td>21.2659</td>
      <td>12406.133674</td>
      <td>NaN</td>
      <td>UNI</td>
      <td>ETH</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-12-01 00:00:00</td>
      <td>57321.4100</td>
      <td>57451.0500</td>
      <td>56814.3400</td>
      <td>56987.9700</td>
      <td>388.482022</td>
      <td>NaN</td>
      <td>BTC</td>
      <td>BTC</td>
    </tr>
  </tbody>
</table>
</div>



basic information of the dataset


```python
data.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 2667 entries, 0 to 2666
    Data columns (total 9 columns):
     #   Column     Non-Null Count  Dtype  
    ---  ------     --------------  -----  
     0   ts         2667 non-null   object 
     1   open       2667 non-null   float64
     2   high       2163 non-null   float64
     3   low        2378 non-null   float64
     4   close      2531 non-null   float64
     5   volume     2667 non-null   float64
     6   volumeUSD  0 non-null      float64
     7   token      2667 non-null   object 
     8   chain      2667 non-null   object 
    dtypes: float64(6), object(3)
    memory usage: 187.6+ KB


we could see above that out of 2667 rows, there are missing (NULL) values of high, low, close and volumneUSD columns


```python
#finding unique values of token
data.token.unique()
```




    array(['SOL', 'COMP', 'AAVE', 'UNI', 'BTC', 'ETH', 'USDT', 'CRV',
           '<span name="tokenName">SOL</span>',
           '<span name="tokenName">ETH</span>',
           '<span name="tokenName">USDT</span>',
           '<span name="tokenName">UNI</span>',
           '<span name="tokenName">BTC</span>',
           '<span name="tokenName">CRV</span>',
           '<span name="tokenName">AAVE</span>',
           '<span name="tokenName">COMP</span>'], dtype=object)



as few tokens are in html format, token names have to be extracted as below


```python
data.loc[data.token.str.contains('span'), 'token'] = data.loc[data.token.str.contains('span'), 'token'].str.extract('<span name="tokenName">(.*?)<\/span>').values
data.token.value_counts()
```




    UNI     342
    BTC     337
    CRV     335
    SOL     334
    USDT    333
    COMP    332
    AAVE    328
    ETH     326
    Name: token, dtype: int64



dropping duplicates


```python
data.drop_duplicates(subset=['ts','chain','token'], inplace=True)
len(data.index)
```




    2360



we could see above that total rows decreased from 2667 to 2360. Hence, duplicates were present.

plotting prices of each token


```python
def plotting(df,cols,nrows,ncols,groupbyColumn=None):
    for t in list(df[groupbyColumn].unique()):
        temp = df[df[groupbyColumn]==t].set_index("ts")
        temp = temp.sort_index()
        fig, axes = plt.subplots(nrows=nrows, ncols=ncols,figsize=(10, 10))
        fig.suptitle(t)
        i = 0
        for param in cols:
            temp[param].plot(ax=axes[i//2, i%2], label=param, rot=30)
            axes[i//2, i%2].legend()
            axes[i//2, i%2].set_title(param)
            i = i+1
        fig.tight_layout()
    
```

plotting raw data for visualising data quality


```python
 plotting(data,["open","high","low","close","volume"],3,2,groupbyColumn="token")
```


    
![png](output_18_0.png)
    



    
![png](output_18_1.png)
    



    
![png](output_18_2.png)
    



    
![png](output_18_3.png)
    



    
![png](output_18_4.png)
    



    
![png](output_18_5.png)
    



    
![png](output_18_6.png)
    



    
![png](output_18_7.png)
    


Through above plots we could see volume and open price data is fine for all the tokens. There are outliers in close price data series of all the tokens. Also, low, high and close price series have missing values. Missing values of the prices will be filled by padding the previous known prices. Outliers in close price will be removed and replaced by mean value of open, high and low prices.


```python
data.set_index("ts",inplace=True)
data["closeReturnsAbsolute"] = abs(data.groupby("token")['close'].pct_change().values) * 100
data.reset_index(inplace=True)
data.tail(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ts</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>volumeUSD</th>
      <th>token</th>
      <th>chain</th>
      <th>closeReturnsAbsolute</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2355</th>
      <td>2021-12-13 06:00:00</td>
      <td>167.48</td>
      <td>167.80</td>
      <td>166.93</td>
      <td>167.64</td>
      <td>11191.365000</td>
      <td>NaN</td>
      <td>SOL</td>
      <td>SOL</td>
      <td>0.089558</td>
    </tr>
    <tr>
      <th>2356</th>
      <td>2021-12-13 06:00:00</td>
      <td>49065.45</td>
      <td>49108.33</td>
      <td>48970.10</td>
      <td>49087.76</td>
      <td>123.274547</td>
      <td>NaN</td>
      <td>BTC</td>
      <td>BTC</td>
      <td>0.045531</td>
    </tr>
    <tr>
      <th>2357</th>
      <td>2021-12-13 06:00:00</td>
      <td>3.87</td>
      <td>3.87</td>
      <td>3.82</td>
      <td>NaN</td>
      <td>45270.080000</td>
      <td>NaN</td>
      <td>CRV</td>
      <td>ETH</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2358</th>
      <td>2021-12-13 06:00:00</td>
      <td>4020.10</td>
      <td>4021.99</td>
      <td>NaN</td>
      <td>4014.90</td>
      <td>1344.134433</td>
      <td>NaN</td>
      <td>ETH</td>
      <td>ETH</td>
      <td>0.129350</td>
    </tr>
    <tr>
      <th>2359</th>
      <td>2021-12-13 06:00:00</td>
      <td>173.83</td>
      <td>174.13</td>
      <td>NaN</td>
      <td>173.99</td>
      <td>415.171000</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.103561</td>
    </tr>
  </tbody>
</table>
</div>



Finding outliers by comparing 50th, 90th, 99th and 99.99th percentile of "closeReturnsAbsolute"


```python
percentileDf = data[["closeReturnsAbsolute","token"]].groupby("token").quantile([0.5,0.95,0.99,0.9999])
percentileDf
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>closeReturnsAbsolute</th>
    </tr>
    <tr>
      <th>token</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="4" valign="top">AAVE</th>
      <th>0.5000</th>
      <td>0.626576</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>3.342678</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9782.116733</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>9901.247673</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">BTC</th>
      <th>0.5000</th>
      <td>0.430662</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>99.001346</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9958.775233</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>966127.473364</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">COMP</th>
      <th>0.5000</th>
      <td>0.653259</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>4.006052</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9879.187469</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>9979.087186</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">CRV</th>
      <th>0.5000</th>
      <td>1.126452</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>99.012167</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>10105.119676</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>10550.998931</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">ETH</th>
      <th>0.5000</th>
      <td>0.452336</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>2.643016</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9756.667236</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>9920.935716</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">SOL</th>
      <th>0.5000</th>
      <td>0.739935</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>98.982963</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9945.735788</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>10044.650886</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">UNI</th>
      <th>0.5000</th>
      <td>0.619302</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>3.923300</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>9793.524882</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>10010.510624</td>
    </tr>
    <tr>
      <th rowspan="4" valign="top">USDT</th>
      <th>0.5000</th>
      <td>0.009989</td>
    </tr>
    <tr>
      <th>0.9500</th>
      <td>0.029968</td>
    </tr>
    <tr>
      <th>0.9900</th>
      <td>99.000021</td>
    </tr>
    <tr>
      <th>0.9999</th>
      <td>9900.000000</td>
    </tr>
  </tbody>
</table>
</div>



removing outliers and replacing with NULL


```python
data['close'].values[data.closeReturnsAbsolute>20.0] = np.nan
data.set_index("ts",inplace=True)

#removing 1st "ts" of "CRV" token as 1st close price is erroneous
data.drop(index=data[data.token=="CRV"].index[0],axis=0,inplace=True)

data["closeReturnsAbsolute1"] = abs(data.groupby("token")['close'].pct_change().values) * 100
data.reset_index(inplace=True)
```

Filling missing values of the prices by padding the prices


```python
data = data.groupby("token").apply(lambda x: x.set_index("ts").ffill().reset_index())
data.reset_index(level=0,drop=True,inplace=True)
```


```python
data.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>ts</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>volumeUSD</th>
      <th>token</th>
      <th>chain</th>
      <th>closeReturnsAbsolute</th>
      <th>closeReturnsAbsolute1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2021-12-01 01:00:00</td>
      <td>257.149</td>
      <td>266.249</td>
      <td>255.270</td>
      <td>264.816</td>
      <td>5752.541</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>3.009981</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2021-12-01 02:00:00</td>
      <td>264.755</td>
      <td>266.187</td>
      <td>262.597</td>
      <td>263.125</td>
      <td>1559.330</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.638557</td>
      <td>0.638557</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2021-12-01 03:00:00</td>
      <td>263.184</td>
      <td>266.187</td>
      <td>262.597</td>
      <td>266.257</td>
      <td>1647.398</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>1.190309</td>
      <td>1.190309</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2021-12-01 04:00:00</td>
      <td>266.384</td>
      <td>267.024</td>
      <td>264.284</td>
      <td>265.502</td>
      <td>829.993</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.283561</td>
      <td>0.283561</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2021-12-01 05:00:00</td>
      <td>265.491</td>
      <td>266.088</td>
      <td>264.000</td>
      <td>265.073</td>
      <td>594.071</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.161581</td>
      <td>0.161581</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2021-12-01 06:00:00</td>
      <td>265.179</td>
      <td>266.107</td>
      <td>262.566</td>
      <td>262.621</td>
      <td>616.346</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.925028</td>
      <td>0.925028</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2021-12-01 07:00:00</td>
      <td>262.816</td>
      <td>266.107</td>
      <td>262.566</td>
      <td>265.498</td>
      <td>1150.309</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>1.095495</td>
      <td>1.095495</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2021-12-01 08:00:00</td>
      <td>265.367</td>
      <td>267.494</td>
      <td>264.519</td>
      <td>267.070</td>
      <td>527.563</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.592095</td>
      <td>0.592095</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2021-12-01 09:00:00</td>
      <td>267.423</td>
      <td>268.591</td>
      <td>263.822</td>
      <td>264.409</td>
      <td>1325.214</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>0.996368</td>
      <td>0.996368</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2021-12-01 10:00:00</td>
      <td>264.425</td>
      <td>267.732</td>
      <td>262.967</td>
      <td>267.344</td>
      <td>360.597</td>
      <td>NaN</td>
      <td>AAVE</td>
      <td>ETH</td>
      <td>1.110023</td>
      <td>1.110023</td>
    </tr>
  </tbody>
</table>
</div>



calculating volumeUSD


```python
data["volumeUSD"] = data["volume"] * data["close"]
#plotting after cleaning data and calculating volumeUSD
plotting(data,["open","high","low","close","volume","volumeUSD"],3,2,groupbyColumn="token")
```


    
![png](output_29_0.png)
    



    
![png](output_29_1.png)
    



    
![png](output_29_2.png)
    



    
![png](output_29_3.png)
    



    
![png](output_29_4.png)
    



    
![png](output_29_5.png)
    



    
![png](output_29_6.png)
    



    
![png](output_29_7.png)
    


calculating volume USD by chain


```python
volumeUSDChain = data.groupby('chain')[['volumeUSD']].sum()
volumeUSDChain.sort_values('volumeUSD', ascending=False, inplace=True)
volumeUSDChain
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>volumeUSD</th>
    </tr>
    <tr>
      <th>chain</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ETH</th>
      <td>1.363751e+10</td>
    </tr>
    <tr>
      <th>BTC</th>
      <td>1.093707e+10</td>
    </tr>
    <tr>
      <th>SOL</th>
      <td>4.061464e+09</td>
    </tr>
    <tr>
      <th>USDT</th>
      <td>1.006272e+09</td>
    </tr>
  </tbody>
</table>
</div>



plotting volumeUSD by chain for visualisation


```python
volumeUSDChain.plot(kind='bar', title='VolumeUSD by Chain',legend=False)
```




    <AxesSubplot:title={'center':'VolumeUSD by Chain'}, xlabel='chain'>




    
![png](output_33_1.png)
    

