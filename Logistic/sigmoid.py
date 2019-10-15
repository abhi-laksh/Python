import numpy as np
import pandas as pd 
import matplotlib.pyplot as grph
def sigmoid(x):

	s = 1/(1+ np.exp(-x))

	return s

def plotGraph(x,y):
	
	grph.scatter(x,y,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")





	grph.show()

path="sample.csv"

data=pd.read_csv(path)

Xi=data["X-cord"]



Yi=sigmoid (Xi)

plotGraph(Xi,Yi)
