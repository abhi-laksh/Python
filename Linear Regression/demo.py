import numpy as np
import matplotlib.pyplot as grph
import pandas as pd
import random


m=2.25646849
c=25.654984536413
x = np.arange(10000)

delta = np.random.uniform(-1000,1000, size=(10000,))

y = m * x + c + delta

def plotGraph(x,y):
	
	

	grph.scatter(x,y,color="#8c7ae6",marker="+" , s=10)

	grph.xlabel("X-cord")
	grph.ylabel("Y-cord")

	grph.show()


plotGraph(x,y)