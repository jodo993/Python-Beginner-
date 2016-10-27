
inputFile = open("input.txt", "r")
outputFile = open("output.txt", "w")
line = inputFile.readline()
i = 1
    
while line != "":
    line = inputFile.readline()
    outputFile.write("/*", i, "*/", line)
    i = i + 1

inputFile.close()
outputFile.close()
