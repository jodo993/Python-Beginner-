# This program has a pre defined list and will
# 1. Swap the first and last elements
# 2. Replace all even elements with a zero
# 3. Return second largest element
# 4. Return true if list is in increasing order

def main() :
    
    ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # Pre-defined list
    data = list(ONE_TEN)                        # Put list in data
        
    print("The original data for all function is: ", ONE_TEN)
    
    # Call swap function
    swapFirstLast(data)
    print("After swapping first and last: ", data)
    print()

    data = list(ONE_TEN) 
    # Call replace zero function
    print("List after all even elements is turned to zero.")
    replaceEvenToZero(data)
    print()

    data = list(ONE_TEN) 
    # Call 2nd largest function

    print("The second largest number in the list is: ")
    returnSecondLargest(data)
    print()

    data = list(ONE_TEN) 
    # Call sort check function
    print("The list is in increasing order: ")
    sortedInIncreasingOrder(data)

# @param data - holds the list
# @param return - send back the list with first and last switched
def swapFirstLast(data) :
    
    extra = data[0]         # Temporary holder for i of 0
    data[0] = data[9]       # Swap the last with first and first with last
    data[9] = extra

    return (data)

# @param data - holds the list
# @param return - return list with all even numbers replaced with zero
# To replace all even indexes with zero change data[i] in if statement to i
def replaceEvenToZero(data) :
    
    for i in range(len(data)) :     # Checks the element, if even turn to zero
        if (data[i] % 2 == 0) :
            data[i] = 0

    return print(data)

# @param data - holds the list
# @param return -     
def returnSecondLargest(data) :
    
    largest = data[0]       # Set both to same value
    second = data[0]
    
    for i in range(1, len(data)) :      # Find the largest first 
        if data[i] > largest :
            second = largest
            largest = data[i]
        elif second < data[i] :         
            second = data[i]
    return print(second)

# @param data - holds the list
# @param return -             
def sortedInIncreasingOrder(data) :

    order = True        # Set to true until condition no longer apply
    start = data[0]
    for i in range(1, len(data)) :      # Compare two indexes number then replace
        if start < data[i] :            # first one with second and recheck
            start = data[i]
        else :
            order = False
    return print(order)

# Start program        
main()
