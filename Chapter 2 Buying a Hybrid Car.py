# This program calculate the cost of owning a car for five years
NUM_YEARS = 5

costNewCar = input("What is the cost of the new car: ")
milesDrivenPerYear = input("How many miles are driven per year: ")
gasPrice = input("What is the gas price: ")
milesPerGallon = input("What is the miles per gallon: ")
resaleValue = input("What is the resale value in 5 years: ")

totalCost = int(costNewCar) - int(resaleValue) + ((NUM_YEARS * int(milesDrivenPerYear))/(int(milesPerGallon) * int(gasPrice)))
print(totalCost)
