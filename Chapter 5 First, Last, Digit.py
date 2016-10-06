# This program will return the first, last, and digit count of a number

# Ask for user input and sends to function
def main():
    number = input("Enter a number: ")
                 
    firstDigit(number)
    lastDigit(number)
    digit(number)

# Finds the first digit in the number
# @param number - number that user enter
# @return - give back the first digit
def firstDigit(number):
    first = int(number[0])
    return print("The first digit is: ", first)

# Finds the last digit in the number
# @param number - number that user enter
# @return - give back the last digit
def lastDigit(number):
    number = int(number)
    last = number % 10
    return print("The last digit is: ", last)

# Finds the total number of digits in the number
# @param number - number that user enter
# @return - give back the total number of digits
def digit(number):
    str(number)
    digit = len(str(number))
    return print("The total number of digits is: ", digit)

# Start the program
main()
