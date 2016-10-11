# This program compares 3 numbers and see if they are the same, different, or sorted

# Ask for user inputs and sends to functions
def main():
    x = int(input("Enter 1st number: "))
    y = int(input("Enter 2nd number: "))
    z = int(input("Enter 3rd number: "))
    allTheSame(x,y,z)
    allDifferent(x,y,z)
    sort(x,y,z)

# Compare the numbers and return true if all same
# @param x,y,z - numbers from user input
# @return - print true if numbers are all the same
def allTheSame(x,y,z):
    same = True
    if x == y and x == z :
        return print(same)
    else :
        print(not same)

# Compare the numbers and return true if all same
# @param x,y,z - numbers from user input
# @return - print true if all numbers are different
def allDifferent(x,y,z):
    different = True
    if x != y and x != z and y != z :
        return print(different)
    else :
        return print(not different)

# Compare the numbers and return true if sorted from least to greatest
# @param x,y,z - numbers from user input
# @return - print true or false if sorted or not sorted
def sort(x,y,z) :
    sort = True
    if x < y and x < z and y < z :
        return print(sort)
    else :
        return print(not sort)

# Start the program
main()
