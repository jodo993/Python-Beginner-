def main():
    number = (input("Enter a number: "))
                 
    firstDigit(number)
    lastDigit(number)
    digit(number)

def firstDigit(number):
    first = int(number[0])
    return print(first)

def lastDigit(number):
    number = int(number)
    last = number % 10
    return print(last)

def digit(number):
    str(number)
    digit = len(str(number))
    return print(digit)

main()
