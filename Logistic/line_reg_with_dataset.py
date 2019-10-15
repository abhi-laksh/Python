import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 

  
def estimate_coef(x, y): 
    # number of observations/points 
    n = np.size(x) 
  
    # mean of x and y vector 
    #m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    #SS_xy = np.sum(y*x - n*m_y*m_x) 
    #SS_xx = np.sum(x*x - n*m_x*m_x) 
    
    nom = (np.sum(x)*np.sum(x*y)) - (np.sum(x**2)*np.sum(y))
    
    denom = ((np.sum(x))**2) - n*(np.sum(x**2))
    
    b_0 = nom/denom
    
    b_1 = (np.sum(y) - (n*b_0))/(np.sum(x))
  
    # calculating regression coefficients 
    #b_1 = SS_xy / SS_xx 
    #b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 
  
def plot_regression_line(x, y, b): 
    # plotting the actual points as scatter plot 
    plt.scatter(x, y, color = "black", 
               marker = "o", s = 50) 
  
    # predicted response vector 
    y_pred = b[0] + b[1]*x 
  
    # plotting the regression line 
    plt.plot(x, y_pred, color = "b") 
  
    # putting labels 
    plt.xlabel('X') 
    plt.ylabel('Y') 
  
    # function to show plot 
    plt.show()
    
def predict(x, b) :
    
    y_pred = b[0] + b[1]*x
    
    print("\n\nThe predicted value of Y : " + str(y_pred))
    
  
def main(): 
    # observations 
    data = pd.read_csv("lr.csv")
    x = data['X-cord']
    y = data['Y-cord']
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {} \nb_1 = {}".format(b[0], b[1])) 
  
    # plotting regression line 
    plot_regression_line(x, y, b)
    
    zz = int(input("Enter a X value to predict : "))
    
    predict(zz,b)
  
if __name__ == "__main__": 
    main() 

