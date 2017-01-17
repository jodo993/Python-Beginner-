#inputFileName = input("Input File: ")
def main():
    
    inFile = open("numberOfCharWordLine.txt", "r")

    totalOne = 0
    totalTwo = 0
    totalThree = 0

    line = inFile.readline()

    while line != "":
        fields = line.split()
        colOne = fields[0]
        colTwo = fields[1]
        colThree = fields[2]
        colOne = float(colOne)
        colTwo = float(colTwo)
        colThree = float(colThree)
        totalOne = add(colOne, totalOne)
        totalTwo = add(colTwo, totalTwo)
        totalThree = add(colThree, totalThree)
        line = inFile.readline()

    print("The sums are:",totalOne,",",totalTwo,",",totalThree)

    inFile.close()

def add(col, total):

    total = total + col
    return total

main()



