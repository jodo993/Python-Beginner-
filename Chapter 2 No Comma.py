# This program takes a number from 10,000-99,999 and removes the comma
userInput = input("Please enter a number from 10,000-99,999: ")

# Takes in user input
userInput = str(userInput)
newNumber = userInput.replace(",","")

print(newNumber)
