# This program reads a sale text file and displays the total amount for
# each service category.
def main():
    try:
        
        inputFile = open("hotelSalesperson.txt", "r")   # Open the file

        totalAmountDinner = 0.0     # Total for dinner and lodging is 0
        totalAmountLodging = 0.0

        line = inputFile.readline()     # Read line

        # Read until end of file
        while line != "":
            fields = line.split(";")        # Split at ;
            if(fields[1] == "Dinner"):      # If matches with dinner, add to total
                colServiceOne = fields[1]
                colAmountDinner = fields[2]
                colAmountDinner = float(colAmountDinner)    # Change to float
                totalAmountDinner = process(colAmountDinner, totalAmountDinner) # Method to find total
                line = inputFile.readline()
            elif(fields[1] == "Lodging"):   # If matches with lodging, add to total
                colServiceTwo = fields[1]
                colAmountLodging = fields[2]
                colAmountLodging = float(colAmountLodging)  # Change to float
                totalAmountLodging = processTwo(colAmountLodging, totalAmountLodging)   # Method to find total
                line = inputFile.readline()
        
        print(colServiceOne,": %.2f" % totalAmountDinner)   # Display
        print(colServiceTwo,": %.2f" % totalAmountLodging)

        inputFile.close()       # Close file

    except Exception as string:
        print("Invalid")

#@param colAmountDinner - one dinner amount
#@param totalAmountDinner - total dinner amount so far
#@return - return total dinner amount
def process(colAmountDinner, totalAmountDinner):
    totalAmountDinner = totalAmountDinner + colAmountDinner
    return totalAmountDinner

#@param colAmountLodging - one lodging amount
#@param totalAmountLodging - total lodging amount so far
#@return - return total Lodging amount
def processTwo(colAmountLodging, totalAmountLodging):
    totalAmountLodging = totalAmountLodging + colAmountLodging
    return totalAmountLodging

# Start program
main()
