inputFile = open("hotelSalesperson.txt", "r")

line = inputFile.readline()
while line != "":
    for line in inputFile:
        substring = line.split(";")
        service = substring[1]
        price = substring[2]
        #line = inputFile.readline()
print(service, price)


