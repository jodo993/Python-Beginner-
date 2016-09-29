# This program finds the minimum value and prints it from a set of inputs

# Initialize the variables
first = True
minimum = 0.0
value = 0.0
value = input("Enter a number or press Enter to stop: ")

# Loop until user press enter
while value != "" :
    value = float(value)
    if first :
        minimum = value
        first = False
    elif value < minimum :
        minimum = value
    value = input("Enter a number or press Enter to stop: ")
print("Minimum is: ", minimum)
