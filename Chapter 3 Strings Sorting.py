# This program reads 3 strings and sort them

# Ask for string
stringOne = input("Enter first word: ")
stringTwo = input("Enter second word: ")
stringThree = input("Enter third word: ")

# Runs through the string and sorts them in order
if stringOne < stringTwo and stringOne < stringThree :
    print(stringOne)
    if stringTwo < stringThree :
        print(stringTwo)
        print(stringThree)
    else :
        print(stringThree)
        print(stringTwo)
elif stringTwo < stringOne and stringTwo < stringThree :
    print(stringTwo)
    if stringOne < stringThree :
        print(stringOne)
        print(stringThree)
    else :
        print(stringThree)
        print(stringOne)
else :
    print(stringThree)
    if stringOne < stringTwo :
        print(stringOne)
        print(stringTwo)
    else :
        print(stringTwo)
        print(stringOne)
    
