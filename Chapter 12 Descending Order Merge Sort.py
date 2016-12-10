# This program sort a group of number with merge sort
# Create random numbers
from random import randint

def main():
    # Create a list of random values
    n = 20
    values = []
    for i in range(n):
        values.append(randint(1,100))
    print(values)
    mergeSort(values)
    print(values)

# Split the list into two and continually pick the lowest number of the two
# and add to sorted list
def mergeSort(values):
    if len(values) <= 1: return
    mid = len(values) // 2
    first = values[ :mid]
    second = values[mid: ]
    mergeSort(first)
    mergeSort(second)
    mergeLists(first, second, values)

# Compare first number of each list and determine smaller
def mergeLists(first,second,values):
    iFirst = 0
    iSecond = 0
    j = 0

    while iFirst < len(first) and iSecond < len(second):
        if first[iFirst] > second[iSecond]:
            values[j] = first[iFirst]
            iFirst = iFirst + 1
        else:
            values[j] = second[iSecond]
            iSecond = iSecond + 1

        j = j + 1

    while iFirst < len(first):
        values[j] = first[iFirst]
        iFirst = iFirst + 1
        j = j + 1

    while iSecond < len(second):
        values[j] = second[iSecond]
        iSecond = iSecond + 1
        j = j + 1

# Start program
main()
