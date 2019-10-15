import numpy as np
import matplotlib.pyplot as grph
import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_excel('lr.xlsx')
data.shape
data.columns
data['width'].unique()

train=data.iloc[:2560, :]
test=data.iloc[2561: , :]

logr= LogisticRegression()

logr.fit(train["width"].values.reshape(-1,1) , train["orange"])

logr.predict(test["width"].values.reshape(-1,1))

x_test=test["width"].values.reshape(-1,1)
y_pred=logr.predict_proba(x_test)

logr.intercept_
logr.coef_

grph.plot(x_test,y_pred)
grph.show()

print(logr.fit(train["width"].values.reshape(-1,1) , train["orange"]))

print(logr.predict(test["width"].values.reshape(-1,1)))
print(logr.predict_proba(test["width"].values.reshape(-1,1)))

print(logr.intercept_)
print(logr.coef_)


