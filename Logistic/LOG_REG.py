# This is Linear regression model
# - - - Coded in UTF-8
#  - - - This is a Linear Regression model with self-defined class (imported as a module named LR_module) 
#  
# !!! Created by @abhi-laksh aka Abhishek Soni
#     on 22nd December 2018 11:35:08 ( GMT + 5:30 )  !!!


import pandas as pd 
import matplotlib.pyplot as grph
from lrMod import LinearReg
import numpy as np

lr=LinearReg()

# Take user input if data is somewhere else 
# path=input("Enter path of csv : ").replace("\\","/")

# Demo File
path="lr.csv"

data=pd.read_csv(path)

Xi=data["width"]
Yi=data["orange"]
# Calculate coeff and intercept of a line

intercpt= lr.intercept(Xi,Yi)
coeff= lr.slope(Xi,Yi,intercpt)

# Defining function to plot a graph
def plotGraph(x):
	

	line = coeff * (x) + intercpt 

	prob= 1 / (1 + np.exp(-x))
	
	grph.scatter(x,prob,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")

	# grph.plot(x,prob,color="#ff4757")


	print("Intercept is : ",intercpt)

	print("Coeffecient is " , coeff)

	print(prob)
	grph.show()


plotGraph(Xi)

# Asking the value of X to predict its Y-cord.

ask_X = float(input("Enter value of x to predict : "))

pred_y=lr.predict(ask_X,intercpt,coeff)

print("Predicted value  : ", pred_y)

# ===   End of the program ===