# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
import pickle

df=pd.read_csv("real estate.csv")
df=df.dropna()
df=df.drop("RAD",axis=1)
col=list(df)
X=df.drop(["MEDV"],axis=1)
y=df["MEDV"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
R=RandomForestRegressor(n_estimators= 100,max_features=5)
R.fit(X_train,y_train)
y_pred=R.predict(X_test)

score=r2_score(y_test,y_pred)
f=open('realestate.pkl','wb')
pickle.dump(R,f)
f.close()