values = []

print("Please enter a list of values: ")
print("To quit, press Q")
userInput = input("")

while userInput.upper() != "Q" :
    values.append(float(userInput))
    userInput = input("")

largest = values[0]
for i in range(1, len(values)) :
    if values[i] > largest :
        largest = values[i]

smallest = values[0]
for i in range(1, len(values)) :
    if values[i] < smallest :
        smallest = values[i]

for element in values :
    print(element, end="")
    if element == largest :
        print(" = largest value", end="")
    print()

for element in values :
    print(element, end="")
    if element == smallest :
        print(" = smallest value", end="")
    print()
