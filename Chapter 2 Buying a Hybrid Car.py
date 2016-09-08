# This program calculate the cost of owning a car for five years
NUM_YEARS = 5

# Takes in data from the user
costNewCar = input("What is the cost of the new car: ")
milesDrivenPerYear = input("How many miles are driven per year: ")
gasPrice = input("What is the gas price: ")
milesPerGallon = input("What is the miles per gallon: ")
resaleValue = input("What is the resale value in 5 years: ")

# Calculate and display result
totalCost = int(costNewCar) - int(resaleValue) + ((NUM_YEARS * int(milesDrivenPerYear))/(int(milesPerGallon) * int(gasPrice)))
print("Total cost of owning a car for five years is",totalCost)
