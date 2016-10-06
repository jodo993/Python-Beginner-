# This program converts letter to number in a telephone number

def main():

    translateNumber()

def translateNumber():
    phoneNumber = input("Enter a string: ")
    phoneNumber = phoneNumber.lower()

    for char in phoneNumber :
        if char in "abc" :
            phoneNumber = phoneNumber.replace(char, '2')
        elif char in "def" :
            phoneNumber = phoneNumber.replace(char, '3')
        elif char in "ghi" :
            phoneNumber = phoneNumber.replace(char, '4')
        elif char in "jkl" :
            phoneNumber = phoneNumber.replace(char, '5')
        elif char in "mno" :
            phoneNumber = phoneNumber.replace(char, '6')
        elif char in "pqrs" :
            phoneNumber = phoneNumber.replace(char, '7')
        elif char in "tuv" :
            phoneNumber = phoneNumber.replace(char, '8')
        elif char in "wxyz" :
            phoneNumber = phoneNumber.replace(char, '9')
        

    print(phoneNumber)

main()
