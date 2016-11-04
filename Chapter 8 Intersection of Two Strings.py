# This program takes two strings and check for same letters
def main():

    # Ask for user input
    print("Enter two strings for comparison.")
    stringOne = input("String 1: ")
    stringTwo = input("String 2: ")

    # Call method
    lettersInBoth(stringOne, stringTwo)

#@param str1 - first string from user
#@param str2 - second string from user
def lettersInBoth(str1, str2):

    # Call method to get set of letters
    setOne = letters(str1)
    setTwo = letters(str2)

    # Find the similar letters
    inBoth = setOne.intersection(setTwo)
    print("The set of letter that is in both is",inBoth)

def letters(string):

    # Create set list
    wordSet = set()

    # Add letters to the set
    for eachLetter in string:
        wordSet.add(eachLetter)
    return wordSet

# Start program
main()
