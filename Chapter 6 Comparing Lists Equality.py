# This program will compare two lists and determine if they are the same or different

def main():
    firstList = []      # Create an empty list
    secondList = []

    # Ask for user input on first list
    print("Please enter first list or Q to quit: ")
    firstInput = input("")

    # Allow user to enter as many elements as they want
    while firstInput.upper() != "Q":
        firstList.append(firstInput)
        firstInput = input("")

    # Ask for user input on second list
    print("Please enter second list or Q to quit: ")
    secondInput = input("")

    # Allow user to enter as many elements as they want
    while secondInput.upper() != "Q":
        secondList.append(secondInput)
        secondInput = input("")

    # Call function to check if equal
    equals(firstList, secondList)

# @param firstList - holds the first list
# @param secondList - holds the second list
# @param return - returns same if all elements match or different if not
def equals(firstList, secondList):
    
    for i in range(0, len(firstList)):      # Loops through the elements in 1st list
        for j in range(0, len(secondList)): # Loops through the elements in 2nd list
            if (firstList == secondList):   # Compares the lists
                return print("Same")
            else:
                return print("Different")
                
main()
