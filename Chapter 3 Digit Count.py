# This program determines how many digits a number has

print("This program will tell you how many digits a number has.")
number = input("Please enter a number: ")

number = int(number)
if number < 0:
    number = number * -1
    
if number < 10:
    print("This number has one digit.")
elif number < 100:
    print("This number has two digit.")
elif number < 1000:
    print("This number has three digit.")
elif number < 10000:
    print("This number has four digit.")
elif number < 100000:
    print("This number has five digit.")
elif number < 1000000:
    print("This number has six digit.")
elif number < 10000000:
    print("This number has seven digit.")
elif number < 100000000: 
    print("This number has eight digit.")
elif number < 1000000000:
    print("This number has nine digit.")
elif number < 10000000000:
    print("This number has ten digit.")
else :
    print("Number is too big")
