# This program reads a set of floating point values
# It then prints the average, smallest, largest, and range

# Initialize the loop
number = input("Enter a number or Press Enter to finish: ")
number = float(number)

# Declare variables
average = 0.0
largest = 0.0
smallest = number
total = 0.0
count = 0

# Runs loop until user press Enter
# Finds max and min
while number != "" :
    number = float(number)
    total = total + number
    count = count + 1
    if number > largest :
        largest = number
    if number < smallest :
        smallest = number
    number = input("Enter a number or Press Enter to finish: ")

# Determines the average and range    
if count > 0 :
    average = total / count
    ranges = largest - smallest
    
print("Average is:  ", average)
print("Smallest is: ", smallest)
print("Largest is:  ", largest)
print("Range is:    ", ranges)

