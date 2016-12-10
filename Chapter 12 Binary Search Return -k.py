# This program search for a number
# Allow random numbers to be generated
from random import randint

def main():
    n = 10      # Number of random numbers
    values = [] # Array of numbers
    # Assign numbers to array
    for i in range(n):
        values.append(randint(1,20))
    print(values)

    # Sort values
    selectionSort(values)
    print(values)

    # Find values
    low = 0
    high = 10
    done = False
    while not done:
        target = int(input("Enter number to search: "))
        if target == -1:
            done = True
        else:
            pos = binarySearch(values,low,high,target)
            if pos == -1:
                print("Not Found")
            else:
                print("Found in position: ", pos)

# Sort numbers from least to greatest
def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i

    return minPos

# Look for number
def binarySearch(values, low, high, target):
    if low < high:
        mid = (low + high) // 2

        # Return if value is found
        if values[mid] == target:
            return mid
        elif values[mid] < target:
            return binarySearch(values, mid + 1, high, target)
        else:
            return binarySearch(values, low, mid - 1, target)

    else:
        #if values[mid] < target:
        return -1

# Start program
main()
        
