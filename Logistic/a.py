
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
# from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

data = pd.read_csv("lr.csv")

X = data['width']
Y = data['orange']

a = np.array(X)
b = np.array(Y)

c=a.reshape(-1,1)
d=b.reshape(-1,1)


plt.scatter(a, b, color = "b", 
               marker = "o", s = 20) 

line = LogisticRegression()
line.fit(c,np.ravel(d))

intercept = line.intercept_

coeff = line.coef_


d_pred = intercept + coeff*c
yi=1/ (1 + np.exp(-d_pred))
# yi=line.predict_proba(d_pred)

# plt.plot(line.predict_proba(yi)[:,1], color = "r") 
plt.plot()

plt.show()
print(yi)
# print(coeff)

# print(line.predict(70))