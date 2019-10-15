import numpy as np
import matplotlib.pyplot as grph
import pandas as pd
import random


n = int(input("Enter num of obv : "))


x=[]
e=[]

y_pred=[]
for i in range(n):
	rdm_x=random.randint(1,18)
	rdm_e=random.randint(19,31)
	rangeX=int(n/rdm_x)
	rangeE=int(n/rdm_e)
	if rangeX!=0 and rangeE!=0:
		
		m=np.random.uniform(rdm_x)
		c=np.random.uniform(random.randint(-50,0),random.randint(0,50))
		x_val=np.random.uniform(random.randint(0,rangeE),random.randint(0,rangeX))
		x.append(x_val)
		err=np.random.uniform(random.randint(-50,0),random.randint( 0,50))
		e.append(err)
		y_val= (m * x_val) + c + err
		y_pred.append(y_val)
		
	else:
		n=n+1
		continue

np.random.shuffle(y_pred)
np.random.shuffle(x)
print(x)
print("_______________________________________________________________")
print(y_pred)

def plotGraph(x,y):
	
	

	grph.scatter(x,y,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")

	grph.show()

# df=pd.DataFrame({'X-cord':x,'Y-cord':y_pred})

plotGraph(x,y_pred)

# path=input("Where to save csv ? : ").replace("\\","/")
# name=input("Name of csv ? : ")

# if path=='':
# 	df.to_csv(name + ".csv")
# elif name=='' :
# 	print("Name cannot be blank")
# else:
# 	df.to_csv(path+ "/" + name + ".csv")