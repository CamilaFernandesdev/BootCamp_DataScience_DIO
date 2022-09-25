"""PROJECT ML
 - Instructor: Prof. DR. Diego Bruno
 - Project 1: Algorithymus of the Machine Learning
 - Library: Matplotlib and Sklearn
 - Create a regression
"""

import matplotlib
import matplotlib.pyplot as plt
import sklearn
from sklearn.datasets import make_regression

#Gerando 200 amostras
#noise = ruído(error)
x, y = make_regression(n_samples=200, n_features=1, noise=30)

#Ploting the regression
plt.scatter(x,y)
plt.show()
