import json

def getTheta():
	try:
		with open("theta.json", "r+") as file:
			data = json.loads(file.read())
			t0 = data["theta0"]
			t1 = data["theta1"]
	except:
		t0 = 0
		t1 = 0
	return t0, t1

def main():
	mileage = "-1"
	while (float(mileage) < 0):
		try:
			mileage = input("Insert your car mileage: ")
		except EOFError:
			print("EOF: Exit Program")
			exit()
		try:
			float(mileage)
		except:
			print("Wrong input")
			mileage = "-1"
		else:
			if (float(mileage) < 0):
				print("Wrong input")
	theta0, theta1 = getTheta()
	if not theta0 and not theta1:
		print("The Model was not trained yet. Please Train it before to get an estimation.")
	estimatePrice = theta0 + (theta1 * float(mileage))
	if (estimatePrice >= 0):
		print(f"Estimate price for {mileage} is {estimatePrice}")
	else:
		print("Mileage out of Scope. The estimate Price is null")

if __name__ == "__main__":
	main()
