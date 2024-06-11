import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
data=pd.read_csv("C:/Users/Administrator/Desktop/Mlops vignesh/practicals/wine-quality.csv")
print(data)
x=data.iloc[:,:-1]
y=data.iloc[:-1]
x_train,y_train,x_test,y_test=train_test_split()