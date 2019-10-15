import numpy as np
from numpy import sum, exp

import matplotlib.pyplot as grph
import pandas as pd
from sklearn.linear_model import LogisticRegression

data=pd.read_excel('lr.xlsx')
data.shape
data.columns
data['width'].unique()
X=data['width'].unique()
Y=data['orange']

train=data.iloc[:2560, :]
test=data.iloc[2561: , :]

n=np.size(data["width"])
print(n)

def strt_line(a,b):
    c=((sum(a)*sum(a*b))-(sum(a**2)*sum(b))) / ((sum(a))**2 - n* sum(a**2))
    m=(sum(b) - n*c)  / sum(a)
    y=m*X+c
    
    return y


for i,j in zip(X,Y):
    y_line=strt_line(i,j)

Yp=np.exp(y_line) /( 1 + np.exp(y_line))




logr= LogisticRegression()

logr.fit(train['width'],train['orange'])
# logr.predict(Yp.reshape(-1,1))
print(Yp)
grph.plot(Yp,Y)
grph.show()