# This program takes two user inputs and prints solutions
print("Please enter two integers.")

# Takes in user inputs
firstInteger = input("First integer is: ")
secondInteger = input("Second integer is: ")

# Total number of integer used
TOTAL_INTEGER = 2

addition = int(firstInteger) + int(secondInteger)
print("Sum is: " + str(addition))

difference = int(firstInteger) - int(secondInteger)
print("Difference is: " + str(difference))

product = int(firstInteger) * int(secondInteger)
print("Product is: " + str(product))

average = (int(firstInteger) + int(secondInteger))/TOTAL_INTEGER
print("Average is: " + str(average))

distance = abs(difference)
print("Distance is: " + str(distance))

maximum = max(firstInteger, secondInteger)
print("Maximum is: " + str(maximum))

minimum = min(firstInteger, secondInteger)
print("Minimum is: " + str(minimum))
