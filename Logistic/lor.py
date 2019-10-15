import numpy as np
# from numpy import sum, exp
import matplotlib.pyplot as grph
import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_csv('lr.csv')

a=data['orange']
b=data['width']

c=np.array(a)
d=np.array(b)



X=c.reshape(-1,1)
Y=d.reshape(-1,1)

train=data.iloc[ :2560, : ]
test=data.iloc[2561 : , : ]

x_test=test['width'].values.reshape(-1,1)



grph.scatter(c,d , color="g", marker=".")

logr=LogisticRegression()

logr.fit(train['width'].values.reshape(-1,1),np.ravel(train['orange']))



 
inter=logr.intercept_
m=logr.coef_

line=m*X + inter

if line.all()>=0.5:
	prob = 1 / ( 1 + np.exp(-line))
else:
	prob = 1 / ( 1 + np.exp(line))

prob_curve=logr.predict_proba(line)[:,1]

print(prob)
grph.plot(X,prob,color="b")
grph.show()
