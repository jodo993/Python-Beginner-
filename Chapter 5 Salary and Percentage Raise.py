# This program sends a prompt to a function and returns the prompt string
# with the floating point number.

# Sends prompt string to function and print the result
def main():
    salary = readFloat("Please enter your salary: ")
    percentageRaise = readFloat("What percentage raise would you like? ")

    print("The salary is ", salary)
    print("The raise percentage is ", percentageRaise)

# Ask user for salary and percentage
# @param prompt - The string literal that is sent to the function
# @return - Sends back the salary or the percent raise
def readFloat(prompt):
    count = 1                   # Allow salary to be asked first
    if count > 0 :
        salary = input(prompt)
        count - 1               # Make next false so percent is asked
        return salary
    else :
        percentageRaise = input(prompt)
        return percentageRaise

# Start the program    
main()
