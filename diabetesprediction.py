# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:52:59 2019

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# matplotlib inline
data = pd.read_csv("./data/pima-data.csv") # import the dATA SET
print(data.head(10))
data.shape
data.head(5)
data.isnull().values.any()
## Correlation
import seaborn as sns
import matplotlib.pyplot as plt
#get correlations of each features in dataset
corrmat = data.corr()
top_corr_features = corrmat.index
plt.figure(figsize=(20,20))
#plot heat map
g=sns.heatmap(data[top_corr_features].corr(),annot=True,cmap="RdYlGn")
data.corr()
diabetes_map = {True: 1, False: 0}
data['diabetes'] = data['diabetes'].map(diabetes_map)
header=data
plt1=plt
plt2=plt
plt3=plt
plt1.scatter(header['num_preg'],header['diabetes'])
plt2.scatter(header['glucose_conc'],header['diabetes'])
plt3.scatter(header['diastolic_bp'],header['diabetes'])
plt.scatter(header['thickness'],header['diabetes'])
plt.scatter(header['insulin'],header['diabetes'])
plt.scatter(header['num_preg'],header['insulin'])
plt.scatter(header['num_preg'],header['glucose_conc'])
plt.scatter(header['age'],header['insulin'])
plt.title('scatter plot insulin vs age')
plt.xlabel('Age')
plt.ylabel('insulin')
plt.show()

diabetes_true_count = len(data.loc[data['diabetes'] == True])
diabetes_false_count = len(data.loc[data['diabetes'] == False])
(diabetes_true_count,diabetes_false_count)
from sklearn.model_selection import train_test_split
feature_columns = ['num_preg', 'glucose_conc', 'diastolic_bp', 'insulin', 'bmi', 'diab_pred', 'age', 'skin']
predicted_class = ['diabetes']

X = data[feature_columns].values
y = data[predicted_class].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=10)
print("total number of rows : {0}".format(len(data)))
print("number of rows missing glucose_conc: {0}".format(len(data.loc[data['glucose_conc'] == 0])))
print("number of rows missing glucose_conc: {0}".format(len(data.loc[data['glucose_conc'] == 0])))
print("number of rows missing diastolic_bp: {0}".format(len(data.loc[data['diastolic_bp'] == 0])))
print("number of rows missing insulin: {0}".format(len(data.loc[data['insulin'] == 0])))
print("number of rows missing bmi: {0}".format(len(data.loc[data['bmi'] == 0])))
print("number of rows missing diab_pred: {0}".format(len(data.loc[data['diab_pred'] == 0])))
print("number of rows missing age: {0}".format(len(data.loc[data['age'] == 0])))
print("number of rows missing skin: {0}".format(len(data.loc[data['skin'] == 0])))
from sklearn.preprocessing import Imputer

fill_values = Imputer(missing_values=0, strategy="mean", axis=0)

X_train = fill_values.fit_transform(X_train)
X_test = fill_values.fit_transform(X_test)
from sklearn.ensemble import RandomForestClassifier
random_forest_model = RandomForestClassifier(random_state=10)

random_forest_model.fit(X_train, y_train.ravel())
predict_train_data = random_forest_model.predict(X_test)
print(predict_train_data)

from sklearn import metrics

print("Accuracy = {0:.3f}".format(metrics.accuracy_score(y_test, predict_train_data)))
 