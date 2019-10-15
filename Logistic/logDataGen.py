import numpy as np
import matplotlib.pyplot as grph
import pandas as pd
import random


c = float(input("Enter intercept : "))
m = float(input("Enter slope : "))
n = int(input("Enter num of obv : "))


p=np.random.choice([0, 1], size=(n,))
# x=np.random.uniform(random.randint(-50,0),random.randint(0,50),n)

e=np.random.uniform(random.randint(-50,0),random.randint(0,50),p.size)

rat= p /(1-p)


x=( (np.log(rat)) - c -e ) / m

print(x,end=" | ")
print(p)
print("_____________________")
print(c)
print("_____________________")
print(m)
print("_____________________")
print(rat)
print("_____________________")

def plotGraph(x,y):
	
	

	grph.scatter(x,y,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")

	grph.show()

df=pd.DataFrame({'X-cord':x,'Y-cord':p})

plotGraph(x,p)

path=input("Where to save csv ? : ").replace("\\","/")
name=input("Name of csv ? : ")

if path=='':
	df.to_csv(name + ".csv")
elif name=='' :
	print("Name cannot be blank")
else:
	df.to_csv(path+ "/" + name + ".csv")