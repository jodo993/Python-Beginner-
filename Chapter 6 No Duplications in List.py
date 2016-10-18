# This program adds non duplicate numbers to a list of ten

values = []     # Create the list
size = 10       # Create the list size

num = input("Enter 10 numbers: ")       # Prompt user input
count = 0                               # To keep track of elements in list
while count < size:                     # Add numbers to it until ten
    values.append(num)
    for i in range(0, len(values)):     # Loop through the element to check for duplicates
        for x in range(i + 1, len(values)):
            if values[i] == values[x]:
                values.pop(x)           # Removes element if same
                count = count - 1
    count = count + 1
    
    if count < size:
        num = input("")

print(values)
    
