# This program returns a set of letters that are not in both string
def main():

    # Prompt user input
    print("Enter two strings.")
    stringOne = input("String 1: ")
    stringTwo = input("String 2: ")

    # Call method to check for letter that is not shown
    notInEither(stringOne, stringTwo)

#@param str1 - first string user entered
#@param str2 - second string user entered
def notInEither(str1, str2):

    alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z"}

    # Create set for each string
    setOne = letters(str1)
    setTwo = letters(str2)
    setTotal = setOne.union(setTwo)
    # Check for letters not contained in both
    notIn = alphabet.difference(setTotal)
    
    print("The set of lowercase letters not in either is",notIn)

#@param string - string user entered
#@return - the set containing all the letters from each string
def letters(string):

    letterSet = set()
    
    for letters in string:
        letterSet.add(letters)
    return letterSet

# Start the program
main()
