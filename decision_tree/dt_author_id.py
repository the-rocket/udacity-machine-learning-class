#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
import numpy as np


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
gnb = GaussianNB()
t0 = time()
gnb.fit(features_train, labels_train) #.predict(features_test)
print("training time:", round(time()-t0, 3), "s")
t0 = time()
pred = gnb.predict(features_test)
print("predict time:", round(time()-t0, 3), "s")
accuracy = gnb.score(features_train, labels_train)
print(labels_train[:10])
print(pred)
print(accuracy)
#########################################################


