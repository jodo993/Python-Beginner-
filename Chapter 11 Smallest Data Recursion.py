# This program finds the smallest element in the list using recursion

def smallest(data):

    # Return smallest
    if len(data) == 1:
        return data[0]

    smallestRest = smallest(data[0:-1])

    print(smallestRest)
    print(data)

    # If the element is the smallest, return
    if smallestRest > data[-1]:
        return data[-1]
    else:
        return smallestRest

# Has list of elements
def main():
    print(smallest([10,12,33,8,52,49,23,14,1]))
    print("Expected: 1")

# Start program
main()
