# This program reads a text file and determines how many times each word
# shows up

def main():

    start = input("Click any key to start program or Q to quit.")
    start = start.upper()
    while start != "Q":
        
        # Read files
        infile = input("Enter file: ")
        inputFile = open(infile, "r")

        # Create dictionary
        count = dict()

        # Read the lines in the file
        line = inputFile.readline()
        wordList = line.split()
    
        # Split the words up and if word is new, add
        # If old, add to list and is equal to one
        while line != "":
            wordList = line.split()
            line = inputFile.readline()
            for singleWord in wordList:
                if singleWord not in count:
                    count[singleWord] = 1
                else:
                    count[singleWord] = count[singleWord] + 1

        print(count)

        start = input("Click any key to start or Q to quit.")
        start = start.upper()
        
# Start the program
main()
