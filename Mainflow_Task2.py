import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv('C:\\Users\\Tanvi\\Desktop\\Main_Flow_Internship\\01.Data Cleaning and Preprocessing.csv')
print(type(data))
print(data.info)
print(data.describe())
data = data.drop_duplicates()
print(data.isnull())
print(data.isnull().sum())
print(data.notnull())
print(data.isnull().sum().sum())

data2 = data.fillna(value=0)
print(data2)

data3 = data.fillna(method ='pad')
print(data3)

data4 = data.fillna(method = 'bfill')
print(data4)

#detect the outliers using IQR
print(data2.columns)
print(data2.drop(['Observation'],axis=1,inplace=True))
print(data2.columns)

Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3-Q1
print(IQR)

data2 = data2[~(data2<(Q1-1.5*IQR))|(data2>(Q3+1.5*IQR)).any(axis=1)]
print(data2)
print(data2.describe())