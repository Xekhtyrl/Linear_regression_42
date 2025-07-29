import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from estimatePrice import getTheta
plt.rcParams['figure.figsize'] = (12.0, 9.0)

def retrieve_data():
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
	X = input_file.iloc[:, 0]
	Y = input_file.iloc[:, 1]
	t0, t1 = getTheta()
	return X, Y, t0, t1

def restructureData(X, Y):
	x = []
	y = []
	for row in X:
		x.append(row)
	for row in Y:
		y.append(row)
	x = np.array(x).reshape(-1, 1)
	return x, y

def compareLine(X, Y, m, c, x, y):
	Y_pred = m*X + c
	plt.scatter(X, Y)
	reg = LinearRegression()
	reg.fit(x,y)
	y_pred = reg.predict(x)
	plt.scatter(X,Y)
	print(f"The r2, determination coefficient, for the trained line is {calculateCoef(X, Y, Y_pred)}")
	print(f"The r2, determination coefficient, for the line calculate with a standard equation is {calculateCoef(X, Y, y_pred)}")
	if m < 0:
		plt.plot([max(X), min(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
		plt.plot([max(X), min(X)], [min(y_pred), max(y_pred)], color='blue')  # regression line
	else:
		plt.plot([min(X), max(X)], [min(Y_pred), max(Y_pred)], color='red')  # regression line
		plt.plot([min(X), max(X)], [min(y_pred), max(y_pred)], color='blue')  # regression line
	plt.show()

def calculateCoef(X, Y, Y_pred):
	n = len(X)
	mean = (1/n) * sum(Y)
	rss = sum (np.pow((Y - Y_pred), 2))
	tss = sum(np.pow((Y - mean), 2))
	r2 = 1 - (rss / tss)
	return r2

def main():
	X, Y, c, m = retrieve_data()
	if not c and not m:
		print("Theta not set, Train your model first!")
		return
	x, y = restructureData(X, Y)
	compareLine(X, Y, m, c, x, y)

if __name__ == "__main__":
	main()