def main():
    values = []

    print("Please enter elements then/or press Q to quit.")
    userInput = input("")

    while userInput.upper() != "Q":
        values.append(userInput)
        
        userInput = input("")

    print("Original list is: ", values)

    swap(values)
    
def swap(values):
    i = 0
    j = len(values) - 1
    while i < j:
        temp = values[i]
        values[i] = values[j]
        values[j] = temp
        i = i + 1
        j = j - 1
    print("Reverse list is: ", values)
    
main()
