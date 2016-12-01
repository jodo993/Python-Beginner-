def smallest(data):

    if len(data) == 1:
        return data[0]

    smallestRest = smallest(data[0:-1])
    print(data)
    print(smallestRest)

    if smallestRest > data[-1]:
        return data[-1]
    else:
        return smallestRest

def main():
    print(smallest([10,12,33,8,52,49,23,14,1]))
    print("Expected: 1")

main()
