# This program counts the number of lines, words, and chars in a file.

def main():

    # Starting number of:
    lines = 0
    words = 0
    chars = 0
    
    inputFile = input("What is file name: ")    # Get file name

    # Open file and use for loop to go over each line,word,char
    infile = open(inputFile, "r")
    for line in infile:
        lines = lines + 1
        words = words + len(line.split())
        chars = chars + len(line)

    # Print result
    print("Total lines: ", lines)
    print("Total words: ", words)
    print("Total chars: ", chars)

# Start program
main()
