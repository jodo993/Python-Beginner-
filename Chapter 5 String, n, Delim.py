# This program returns a string n amount of times and separated by another string

# Call the repeat function
def main() :
    print(repeat("ho", 3, ","))

# Set up the order of the string
# @param string - the string
# @param n - number of repeats
# @param delim - separates the string
# @return - sends back result
def repeat(string, n, delim) :
    output = ""
    for i in range(3) :
        output = output + string + delim
    return output

# Start the program    
main()
