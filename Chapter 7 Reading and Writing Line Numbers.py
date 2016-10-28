# This program reads a file and adds line number to each line
# Open file to read and write
inputFile = open("maryLamb.txt", "r")
outputFile = open("output.txt", "w")

# i keeps track of lines
i = 1
line = inputFile.readline()

# If not blank, add lines number to each line
while line != "":
    print("/*", i, "*/", line, file=outputFile)
    line = inputFile.readline()
    i = i + 1

# Close files
inputFile.close()
outputFile.close()
