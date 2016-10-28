# This program reads a file containing two columns of numbers and print the
# average of each column
def main():

    inputFile = open("twocolumnaverages.txt", "r")  # Open file
    totalOne = 0.0      # Current total for column one
    totalTwo = 0.0      # Current total for column two
    count = 0           # Keep track of how many numbers in a column
    
    line = inputFile.readline()

    # Read til the end of file
    while line != "":
        fields = line.split()
        colOne = fields[0]
        colTwo = fields[1]
        colOne = float(colOne)  # Convert string to float
        colTwo = float(colTwo)
        count = count + 1
        totalOne = process(colOne, totalOne)    # Call method to find total
        totalTwo = process(colTwo, totalTwo)
        line = inputFile.readline()

    totalOne = totalOne / count         # Find average
    totalTwo = totalTwo / count
    print("The averages are", totalOne, "and", totalTwo)
    
    inputFile.close()       # Close file

#@param col - column number
#@param total - most recent total
#@return - return the total
def process(col, total):
    
    total = total + col
    return total

# Start program
main()
