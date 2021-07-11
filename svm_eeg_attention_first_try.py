import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC

data = pd.read_csv('frequency_parameters_1.csv', sep=',')

print (data.head)

print (data.shape)

target = data[['target_class']]

X = data.drop('target_class', axis=1)

y = data['target_class']

# split X and y into training and testing sets
#
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# check the shape of X_train and X_test

print (X_train.shape, X_test.shape)

#import SVC classifier
from sklearn.svm import SVC

#import metrics to compute accuracy
from sklearn.metrics import accuracy_score

# instantiate classifier with rbf kernel and C=100
svc=SVC(C=100.0) 

# fit classifier to training set
svc.fit(X_train,y_train)

# make predictions on test set
y_pred=svc.predict(X_test)
#
# compute and print accuracy score
print('Model accuracy score with rbf kernel and C=100.0 : {0:0.4f}'. format(accuracy_score(y_test, y_pred)))

