def main() :
    
    ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data = list(ONE_TEN)
    
    print("The original data for all function is: ", ONE_TEN)
    swapFirstLast(data)
    print("After swapping first and last: ", data)

    print("List after all even elements is turned to zero.")
    replaceEvenToZero(data)

    print("The second largest number in the list is: ", data)
    #returnSecondLargest(data)

    sortedInIncreasingOrder(data)
    
def swapFirstLast(data) :
    
    extra = data[0]
    data[0] = data[9]
    data[9] = extra

    return (data)
    
def replaceEvenToZero(data) :
    
    for i in range(len(data)) :
        if (data[i] % 2 == 0) :
            data[i] = 0

    return print(data)
    
def returnSecondLargest(data) :
    
    largest = data[0]
    second = none
    for i in range(1, len(data)) :
        if value[i] > largest :
            largest = value[i]
        elif value[i] :
            largest = value[i]
            
def sortedInIncreasingOrder(data) :

    order = True 
    start = data[0]
    i = 1
    for i in range(len(data)) :
        if start < data[i] :
            start = data[i]
            return print(i)
        else :
            return print(not order)
main()
