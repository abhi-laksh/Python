import numpy as np
# import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.linear_model import LogisticRegression
# sns.set()

x = np.linspace(-2, 2, 400).reshape((400,1))
y = np.vstack((np.zeros(200), np.ones(200))).reshape((400,1))

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.4, random_state=0)

logistic_regr = LogisticRegression()
logistic_regr.fit(x_train, y_train)

fig, ax = plt.subplots()

ax.set(xlabel='x', ylabel='y')
ax.plot(x_test, logistic_regr.predict_proba(x_test)[:,1], '.', label='Logistic regr')  
#ax.plot(x_test,logistic_regr.predict(x_test), label='Logistic regr')
ax.legend()