
def main():
    infile = input("Enter file: ")
    inputFile = open(infile, "r")

    count = dict()
    line = inputFile.readline()
    wordList = line.split()
    while line != "":
        wordList = line.split()
        line = inputFile.readline()
        for singleWord in wordList:
            if singleWord not in count:
                count[singleWord] = 1
            else:
                count[singleWord] = count[singleWord] + 1

    print(count)

main()
