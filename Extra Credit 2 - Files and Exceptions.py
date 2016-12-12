def main():

    lines = 0
    words = 0
    chars = 0
    
    inputFile = input("What is file name: ")

    infile = open(inputFile, "r")
    for line in infile:
        lines = lines + 1
        words = words + len(line.split())
        chars = chars + len(line)

    print("Total lines: ", lines)
    print("Total words: ", words)
    print("Total chars: ", chars)
    
main()
