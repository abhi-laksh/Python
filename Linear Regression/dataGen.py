import numpy as np
import matplotlib.pyplot as grph
import pandas as pd
import random


print(random.randint(0,20))
c = float(input("Enter intercept : "))
m = float(input("Enter slope : "))
n = int(input("Enter num of obv : "))


x=np.random.uniform(random.randint(-50,0),random.randint(0,50),n)

e=np.random.uniform(random.randint(-50,0),random.randint(0,50),x.size)


y_pred=m*x + c + e

print(x,end=" | ")
print(y_pred)

def plotGraph(x,y):
	
	

	grph.scatter(x,y,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")

	grph.show()

df=pd.DataFrame({'X-cord':x,'Y-cord':y_pred})

plotGraph(x,y_pred)

path=input("Where to save csv ? : ").replace("\\","/")
name=input("Name of csv ? : ")

if path=='':
	df.to_csv(name + ".csv")
elif name=='' :
	print("Name cannot be blank")
else:
	df.to_csv(path+ "/" + name + ".csv")