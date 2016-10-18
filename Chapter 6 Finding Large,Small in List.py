# This program will find the largest and smallest number in the list

values = []     # Create an empty list

print("Please enter a list of values: ")        # Prompt user input
print("To quit, press Q")
userInput = input("")

while userInput.upper() != "Q" :        # Allow user to enter as many numbers as they want
    values.append(float(userInput))
    userInput = input("")

largest = values[0]         # Set largest value starting point at sub 0
for i in range(1, len(values)) :    # Loops through list, if larger than holder is new largest
    if values[i] > largest :
        largest = values[i]

smallest = values[0]        # Set smallest value starting point at sub 0
for i in range(1, len(values)) :    # Loops through list, if smaller than holder is new smallest
    if values[i] < smallest :
        smallest = values[i]

for element in values :     # Mark the spot where largest number is at 
    print(element, end="")
    if element == largest :
        print(" = largest value", end="")
    print()

for element in values :     # Mark the spot where smallest number is at 
    print(element, end="")
    if element == smallest :
        print(" = smallest value", end="")
    print()
