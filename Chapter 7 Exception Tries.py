# This program ask user to input float numbers
# After two invalids, display total sum of valid inputs

ok = True           # Start out as true
total = 0.0         # Initialized to 0
tries = 2           # Two tries

# Ask first input
print("Enter a set of floating point numbers.")
print("After two chances, will add up total sum.")
numbers = input("")

# While tries still good, do
while ok:
    try:
        numbers = float(numbers)
        total = total + numbers
        numbers = input("")
    except Exception as string:
        print("Invalid")
        tries = tries - 1
        if (tries == 0):        # No more tries set of false
            ok = False
        if tries > 0:
            numbers = input("")
        
# Display sum
print("Total is: ", total)
            
                
        
        
