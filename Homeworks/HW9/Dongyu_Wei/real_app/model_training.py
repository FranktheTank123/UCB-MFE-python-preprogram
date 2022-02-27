from cmath import pi
from sklearn.model_selection import TimeSeriesSplit
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, make_scorer
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
from functools import reduce
from sklearn import datasets
import pickle
import click


from model_definition import pipeline



dataset_dic = {'digits':datasets.load_digits(),'iris':datasets.load_iris(),'breast_cancer':datasets.load_breast_cancer()}
def preping_data(dataset_name):
    data = dataset_dic[dataset_name]
    X = data.data
    y = data.target
    X_train,X_test,y_train,y_test = train_test_split(data.data,data.target,train_size=0.7,random_state=0)
    return X_train,X_test,y_train,y_test
    


@click.command()
@click.option('--dataset-name')
@click.option('--model-path')
def main(dataset_name, model_path):
    assert dataset_name and model_path, "need to provide valid data path and model path"

    X_train,X_test,y_train,y_test = preping_data(dataset_name=dataset_name)
    print(f"preping data complete, X: {X_train.shape} y: {y_train.shape}")

    pipeline.fit(X_train,y_train)
    best_model = pipeline
 

    # pickle.dump(best_model, open('/Users/tianyixia/dev/UCB-MFE-python-preprogram/data/trained_model.pckl', 'wb'))
    pickle.dump(best_model, open(model_path, 'wb'))


if __name__ == '__main__':
    main()
