def main():

    print("Enter two strings for comparison.")
    stringOne = input("String 1: ")
    stringTwo = input("String 2: ")

    lettersInBoth(stringOne, stringTwo)

def lettersInBoth(str1, str2):

    letters(str1)
    letters(str2)
    inBoth = str1.intersection(str2)
    print(inBoth)

def letters(string):

    string3 = set(string)
    return string3
    
main()
