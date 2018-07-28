"""This program follows one-vs-rest approach of predicting the query used to find a job posting.
It predicts whether the query used to search a particular job posting was same as target_query or not."""

import pandas as pd
import numpy as np
from collections import Counter
from sklearn import tree, svm
from sklearn.metrics import accuracy_score


df = pd.read_csv('New.csv')  # Reading the data. BTW, why is it named New.csv?

# Target_query can be set to any of the ['data engineer', 'data
# scientist', 'deep learning', 'data analyst', 'machine
# learning','software engineering', 'web developer']. Change the
# target_query variable value to see the accuracy of other classes.
target_query = 'deep learning'

# Create a new column target_query and set 1s or 0s based on whether Query
# attribute is same as target_query or not
df[target_query] = df['Query'].apply(lambda x: int(target_query == x))
del df['Query']  # deleting useless columns

# Seperating training and testing data
msk = np.random.rand(len(df)) < 0.8
train = df[msk]
test = df[~msk]
y = train[target_query]
del train[target_query]  # There goes another useless column
X = train.as_matrix()
r = test[target_query]
del test[target_query]  # One more useless column

# Running SVM
clf = svm.SVC()
clf = clf.fit(X, y)  # Feeding training data to the classifier
p = clf.predict(test.as_matrix())

print(accuracy_score(r, p))  # Accuracy of prediction
