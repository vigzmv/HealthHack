# import numpy as np
import os

import pandas as pd
import pickle

from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

def model_liver(dataset="./indian_liver_disease.csv"):
    if(os.path.exists(os.path.join(os.path.dirname(__file__), 'liver_model.pickle'))):
        with open('liver_model.pickle', 'rb') as handle:
            clf = pickle.load(handle)
    else:
        clf = KNeighborsClassifier()
        df = pd.read_csv(dataset, names=['age', 'gender', 'tb', 'db', 'alkphos', 'sgpt', 'sgot', 'tp', 'albumin', 'a/g', 'label']).dropna()
        # X_train, X_test, y_train, y_test = train_test_split(df.ix[:,:-1], df.ix[:,-1:])
        X_train, y_train = df.ix[:,:-1], df.ix[:,-1:]
        clf.fit(X_train, y_train)
    return clf
