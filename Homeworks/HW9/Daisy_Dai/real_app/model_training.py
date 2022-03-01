import pandas as pd
import pickle
from sklearn.utils import shuffle
from sklearn.model_selection import GridSearchCV

from model_definition import pipeline

def prep_data(data_path):
    iris_data = pd.read_pickle(data_path)
    x = iris_data['data']
    y= iris_data['target']
    x,y = shuffle(x, y, random_state=0) #shuffle the data
    names = iris_data['target_names']
    
    return x,y, names

data_path = 'C:/Users/15103/OneDrive/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Daisy_Dai/data/iris_data.pckl'
model_path = 'C:/Users/15103/OneDrive/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Daisy_Dai/data/trained_model.pckl'

def main(data_path, model_path):
    assert data_path and model_path, "need to provide valid data path and model path"
    
    x,y,names = prep_data(data_path)
    print(f"preping data complete, x: {x.shape} y: {y.shape}")
    

    search = GridSearchCV(pipeline, {
        'knn__n_neighbors': [8, 9, 10, 11, 12, 13, 14, 15],
        'knn__p':[1,2]
    }, scoring='accuracy', refit=True, n_jobs=-1)
    
    search.fit(x, y)
    
    best_model = search.best_estimator_
    print(f"model training done. Best params: {search.best_params_}")
    
    pickle.dump(best_model, open(model_path, 'wb'))

if __name__ == '__main__':
    main(data_path, model_path) 
    








