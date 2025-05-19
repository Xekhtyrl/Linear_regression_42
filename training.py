import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
plt.rcParams['figure.figsize'] = (12.0, 9.0)

def retrieve_data():
	data = pd.read_csv('data1.csv')
	X = data.iloc[:, 0]
	Y = data.iloc[:, 1]
	return X, Y

def scale_X():
	n = len(X)
	mean = (1/n) * sum(X)
	std = np.sqrt(1/(n - 1) * sum((X - mean) **2) )
	X_s = (X - mean) / std
	return X_s



# Building the model
m = 0
c = 0

L = 0.001  # The learning Rate
itera = 100000  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
for i in range(itera): 
	Y_pred = m*X_s + c  # The current predicted value of Y
	D_m = (1/n) * np.sum(X_s * (Y_pred - Y))  # Derivative wrt m
	D_c = (1/n) * np.sum(Y_pred - Y)  # Derivative wrt c
	# print(Y_pred, Y)
	m = m - L * D_m  # Update m
	c = c - L * D_c  # Update c
	# print(f"m = {m} > L * D_m = {D_m}, c = {c} > L * D_c = {D_c}")
    
print (m, c)
m = m/std
c = c - (mean * m)
print (m, c)

# Making predictions
x = []
y = []
for row in X:
	x.append(row)
for row in Y:
	y.append(row)
x = np.array(x).reshape(-1, 1)
Y_pred = m*X + c
print(X)
plt.scatter(X, Y)
reg = LinearRegression()
reg.fit(x,y)
y_pred = reg.predict(x)
plt.scatter(X,Y)
plt.plot([max(X), min(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
plt.plot([max(X), min(X)], [min(y_pred), max(y_pred)], color='blue')  # regression line
plt.show()