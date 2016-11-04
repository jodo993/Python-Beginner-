# This program takes a string and returns a set of letters
def main():

    # Ask for a string
    string = input("Please enter a string: ")

    # Call method
    letters(string)

#@param str1 - string from user
def letters(str1):

    # Loops through string and print individual letter
    for letters in str1:
        print(letters)

# Start program
main()
