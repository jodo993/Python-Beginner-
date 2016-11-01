def main():

    print("Enter two strings.")
    stringOne = input("String 1: ")
    stringTwo = input("String 2: ")

    letters(stringOne)
    letters(stringTwo)
    notInEither(stringOne, stringTwo)

def letters(string):

    letter = set()
    
    for letters in string:
        letter = letter.add(letters)
        return letter

def notInEither(str1, str2):

    notIn = str1.difference(str2)
    print(notIn)

main()
