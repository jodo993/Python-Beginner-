infile = open("hello.txt", "w")

infile.write("Hello, World! \n")
infile.close()

infile = open("hello.txt", "r")
message = infile.readline()

while message != "":
    print(message)
    message = infile.readline()
    
infile.close()
