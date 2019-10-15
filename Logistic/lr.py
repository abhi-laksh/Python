import numpy as np
import pandas as pd
import matplotlib.pyplot as grph 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("lr.csv")

c = data['width']
d = data['orange']

a = np.array(c)
b = np.array(d)

X=a.reshape(-1,1)
Y=b.reshape(-1,1)

train=data.iloc[:2560, :]

test=data.iloc[2561: , :]


grph.scatter(a, b, color = "b", 
               marker = "o", s = 20) 

logr = LogisticRegression()
logr.fit(X,Y)



intercept = logr.intercept_

coeff = logr.coef_


y_logr = intercept + coeff*X

d_pred= 1 / (1 + np.exp(-y_logr))



# grph.plot(d_pred, color = "r") 

print(d_pred)

logr.fit(X,d_pred)


# print(Yp)
grph.plot(X,d_pred)
grph.show()
# print(logr.predict())