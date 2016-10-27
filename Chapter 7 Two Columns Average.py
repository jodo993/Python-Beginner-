fileName = input("Enter a file name: ")

infile = open(fileName, "r")

totalOne = 0.0
totalTwo = 0.0
count = 0

for line in infile:
    column = line.split()
    if len(column) > 1:
        totalOne = float(column[0])
        totalTwo = float(column[1])
        count = count + 1

averageOne = totalOne / count
averageTwo = totalTwo / count
print("The averages are ", averageOne, "and ", averageTwo)
