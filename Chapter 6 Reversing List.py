# This program reverses the list order

def main():
    values = []     # Create empty list

    print("Please enter elements then/or press Q to quit.") # Prompt input
    userInput = input("")

    while userInput.upper() != "Q":     # Adds user input into list
        values.append(userInput)
        userInput = input("")

    print("Original list is: ", values) # Display original list

    swap(values)        # Calls function

# @param values - holds the list    
def swap(values):
    i = 0                   # Start of list
    j = len(values) - 1     # End of list
    while i < j:            # Until they meet midpoint continue loop
        temp = values[i]    # Temp holds first number for swap to happen
        values[i] = values[j]
        values[j] = temp
        i = i + 1           # Increment and decrement i and j
        j = j - 1
    print("Reverse list is: ", values)

# Start the program    
main()
