# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:52:19 2018

@author: sampr
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression

data = pd.read_csv("lr.csv")

X = data['width']
Y = data['orange']

a = np.array(X)
b = np.array(Y)

c=a.reshape(-1,1)
d=b.reshape(-1,1)


plt.scatter(a, b, color = "b", 
               marker = "o", s = 20) 

line = LinearRegression().fit(c,d)


intercept = line.intercept_

coeff = line.coef_


d_pred = intercept + coeff*c

plt.plot(c, d_pred, color = "r") 

print(intercept)
print(coeff)

print(line.predict(70))
# print(line.predict(70))
plt.show()