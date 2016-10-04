# This program decide if a number is zero, positive, or negative.
# It also determine if the number is small or large

# Prompt user input
number = input("Please enter a number: ")
number = float(number)

# Determines if number is 0, +, or -
if number == 0:
    print("Zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")

# Determines if the value is large or small
absoluteValue = abs(number)
absoluteValue = float(absoluteValue)
if absoluteValue < 1:
    print("Small")
elif absoluteValue > 1000000:
    print("Large") 
