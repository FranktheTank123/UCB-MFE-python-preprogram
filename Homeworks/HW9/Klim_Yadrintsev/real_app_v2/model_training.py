#importing libraries
import sklearn
import pandas as pd
import seaborn as sns
import keras as K
import keras.layers as Dense
import keras.models as Sequential
import keras.optimizers as Adam
import numpy as np

import pickle

from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

from model_definition import pipeline


# this is just copying from Lecture 8's notebook
def preping_data(data_location) -> tuple[pd.DataFrame, pd.Series]:
    # this should be a global variable
    # data_location = 'sqlite:////Users/tianyixia/dev/UCB-MFE-python-preprogram/data/data.db'
    data = pd.read_sql('SELECT * FROM avocado', data_location)

    data = data.iloc[:, 1:]
    y = data.AveragePrice
    data.drop(['AveragePrice'], axis=1, inplace=True)
    data = data.astype(
        {'Date': 'object', 'Total Volume': 'float64', '4046': 'float64', '4225': 'float64', '4770': 'float64',
         'Total Bags': 'float64', 'Small Bags': 'float64', 'Large Bags': 'float64', 'XLarge Bags': 'float64',
         'type': 'object', 'year': 'int', 'region': 'object'})
    X = data

    return X, y

class ReturnValue:
  def __init__(self, trainflights, testflights, ytrain, ytest, oneHot):
     self.trainflights = trainflights
     self.testflights = testflights
     self.ytrain = ytrain
     self.ytest = ytest
     self.oneHot = oneHot

# defining a way to find Mean Absolute Percentage Error:
def PercentError(preds, ytest):
    error = abs(preds - ytest)

    errorp = np.mean(100 - 100 * (error / ytest))

    print('the accuracy is:', errorp)


def data_prep_prediction(data_path):
    assert data_path, "need to provide valid data path and model path"

    X, y = preping_data(data_location=data_path)
    print(f"preping data complete, X: {X.shape} y: {y.shape}")

    test_size = 0.2
    trainflights, testflights, ytrain, ytest = train_test_split(X, y, train_size=0.7, test_size=0.3, random_state=0)
    s = (trainflights.dtypes == 'object')
    object_cols = list(s[s].index)

    n = (trainflights.dtypes == ('float64', 'int64'))
    numerical_cols = list(n[n].index)
    oneHot = OneHotEncoder(handle_unknown='ignore', sparse=False)
    oneHottrain = pd.DataFrame(oneHot.fit_transform(trainflights[object_cols]))
    oneHottest = pd.DataFrame(oneHot.transform(testflights[object_cols]))

    # reattaching index since OneHotEncoder removes them:
    oneHottrain.index = trainflights.index
    oneHottest.index = testflights.index

    # dropping the old categorical columns:
    cattraincol = trainflights.drop(object_cols, axis=1)
    cattestcol = testflights.drop(object_cols, axis=1)

    # concatenating the new columns:
    trainflights = pd.concat([cattraincol, oneHottrain], axis=1)
    testflights = pd.concat([cattestcol, oneHottest], axis=1)

    trainf = trainflights.values
    testf = testflights.values

    minmax = MinMaxScaler()

    trainflights = minmax.fit_transform(trainf)
    testflights = minmax.transform(testf)

    return ReturnValue(trainflights, testflights, ytrain, ytest, oneHot)




# @click.command()
# @click.option('--data-path')
def main(data_path = 'sqlite:///data_v2/avocado.db'):
    assert data_path, "need to provide valid data path and model path"

    trainflights, testflights, ytrain, ytest, oneHot = data_prep_prediction(data_path)

    # implementing the algo:
    model = RandomForestRegressor(n_estimators=100, random_state=0, verbose=1)

    # fitting the data to random forest regressor:
    model.fit(trainflights, ytrain)

    preds = model.predict(testflights)

    ytest = ytest.astype('float')

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(model, open('E:/programming/python/UCB-MFE-python-preprogram/Homeworks/HW9/Klim_Yadrintsev/data_v2/model.pkl', 'wb'))


if __name__ == '__main__':
    main()
