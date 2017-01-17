def main():

    TEST_LIST = [5,6,7,8,9,10]

    print(TEST_LIST)
 
    print(shift(TEST_LIST))
    
def shift(testList):

    length = len(testList)
    testList = testList[length - 1:] + testList[:length - 1]
    return testList

main()

