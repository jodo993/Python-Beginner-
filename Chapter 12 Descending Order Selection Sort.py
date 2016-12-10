# Program sort a list of values with selection sort
# Create random numbers
from random import randint

def main():
    # Create a list of random numbers
    n = 20
    values = []
    for i in range(n):
        values.append(randint(1,100))
    print(values)
    selectionSort(values)
    print(values)

# Compare find smaller number then swap its position to next uncheck
# part of the list
# Temp holds the value that is being switched
def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values,i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp

def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] > values[minPos]:
            minPos = i

    return minPos

# Start program
main()
