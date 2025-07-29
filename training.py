import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
plt.rcParams['figure.figsize'] = (12.0, 9.0)

def retrieveData():
	try:
		file = input('filePath:')
		if not file:
			file = 'data.csv'
	except EOFError:
		print("\nEOF: data.csv set as default file")
		file = 'data.csv'
	try:
		input_file = pd.read_csv(file)
	except:
		print("Error: Invalid file")
		exit()
	# for row in input_file:
	X = input_file.iloc[:,0]
	Y = input_file.iloc[:,1]
	return X, Y

def scaleX(X):
	n = len(X)
	mean = (1/n) * sum(X)
	std = np.sqrt(1/(n) * sum((X - mean) **2) )
	X_s = (X - mean) / std
	return X_s, mean, std



# Building the model
def gradientDecent(X_s, Y):
	theta1 = 0
	theta0 = 0
	while (True):
		try:
			L = input("Desired Learning rate(has to be between 0.0000...1 and 0.999...:)")# The learning Rate
		except EOFError:
			L = 0.001
			print("\nEOF: Default value set to 0.0001 for Learning rate.")
		try:
			L = float(L)
			if (L > 0) and L < 1:
				break
			print("Value has to be between 0.0...01 and 0.999...")
		except:
			print("value has to be a number")
	while (True):
		try:
			itera = input("Desired iteration(has to be positive):")  # The number of iterations to perform gradient descent
		except EOFError:
			itera = 1000
			print("\nEOF: default value set to 1000 for the number of Iteration.")
		try:
			itera = int(itera)
			if (itera > 0) and itera < 1000000:
				break
			print("value has to be higher than 0 and can not be higher than 1 million")
		except:
			print("value has to be an integer")

	n = float(len(Y)) # Number of elements in X

	# Performing Gradient Descent 
	for i in range(itera): 
		Y_pred = theta1*X_s + theta0  # The current predicted value of Y
		D_theta1 = (1/n) * np.sum(X_s * (Y_pred - Y))  # Derivative wrt m
		D_theta0 = (1/n) * np.sum(Y_pred - Y)  # Derivative wrt c
		theta1 = theta1 - L * D_theta1  # Update m
		theta0 = theta0 - L * D_theta0  # Update c
	return theta0, theta1

def descale_theta(theta0, theta1, std, mean):
	theta1 = theta1/std
	theta0 = theta0 - (mean * theta1)
	return theta1, theta0

def showScatterDot(X, Y, m, c):
	Y_pred = m*X + c
	plt.scatter(X,Y)
	if m < 0:
		plt.plot([max(X), min(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
	else:
		plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
	plt.show()
	return Y_pred

def saveTheta(t0, t1):
	with open("theta.json", "w") as file:
		file.write(json.dumps({"theta0": t0, "theta1": t1}, indent= 4))
	

def main():
	X, Y = retrieveData()
	X_s, mean, std = scaleX(X)
	theta0, theta1 = gradientDecent(X_s, Y)
	theta1, theta0 = descale_theta(theta0, theta1, std, mean)
	Y_pred = showScatterDot(X, Y, theta1, theta0)
	saveTheta(theta0, theta1)

if __name__ == "__main__":
	main()