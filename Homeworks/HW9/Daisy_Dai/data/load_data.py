from sklearn.datasets import load_iris
import pickle 

iris=load_iris()
data_path = 'C:/Users/15103/OneDrive/Desktop/UCB-MFE-python-preprogram/Homeworks/HW9/Daisy_Dai/data/iris_data.pckl'
pickle.dump(iris, open(data_path, 'wb'))

