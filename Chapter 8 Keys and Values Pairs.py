# This program print all the keys, values, and key and value paris
def main():

    # Starting dictionary
    gradeCount = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}

    # Print the keys only
    print("Keys:")
    for key in gradeCount:
        print(key)

    # Print values only
    print("Values:")
    valueList = []
    for value in gradeCount.values():
        valueList.append(value)
        print(value)
    # Print both
    print("All key & value pairs: ", gradeCount)

# Start program
main()
