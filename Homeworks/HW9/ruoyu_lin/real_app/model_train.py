import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from xgboost import XGBRegressor
import pickle
import click
import os
from model_define import pipeline

dir_data = os.getcwd().replace("real_app", "data")

def prep_data(data_path) -> tuple[pd.DataFrame, pd.Series]:
    
    # The generation of data file uses kucoin api, yfinance and forex python. See EDA notebook for 
    # the whole process of data ingestion. 
    
    data = pd.read_csv(data_path)
    data = data.set_index("Date")
    X_cols = [x for x in data.columns if (x[0] == "r" and "lag" not in x) 
                  or ("hh14" in x)
                  or ("ll14" in x)
                  or ("lag" in x)
                  or ("vol_" in x)]
    X = data.loc[:,X_cols].iloc[:-1,:]
    print("Xshape", X.shape)
    y = data.rbtc.shift(-1).iloc[:-1]
    return X, y

@click.command()
@click.option('--data-path')
@click.option('--model-path')

def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"
    X, y = prep_data(data_path = data_path)
    
    test_size = 2
    train_size = 50
    scorer = make_scorer(mean_squared_error, 
                     greater_is_better=False, squared=False)
    cv = TimeSeriesSplit(n_splits=len(X)//test_size-1, test_size = test_size, 
                     gap = -1)
    print("Beginning training...")
    print()
    print("Input head")
    print()
    print(X.head(5))
    search = GridSearchCV(pipeline, {
        "model__learning_rate": [0.08,0.085,0.9], 
        'model__max_depth': [10,12,14], 
        "model__reg_alpha": [0.00005, 0.0001], 
#         "model__reg_gamma": [0.00005, 0.0001]
    }, scoring=scorer, refit=True, cv=cv, n_jobs=-1)
    search.fit(X, y)
    best_model = search.best_estimator_
    print(f"Finished training. Best params: {search.best_params_}")
    pickle.dump(best_model, open(model_path, "wb"))

if __name__ == "__main__":
    main()