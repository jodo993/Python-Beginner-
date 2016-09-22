# This program determines if three numbers are the same or different

# Prompt user input
firstInteger = float(input("Enter 1st number: "))
secondInteger = float(input("Enter 2nd number: "))
thirdInteger = float(input("Enter 3rd number: "))

# Compare the numbers
if firstInteger == secondInteger and secondInteger == thirdInteger :
    print("All the same.")
elif firstInteger != secondInteger and firstInteger != thirdInteger and secondInteger != thirdInteger :
    print("All different")
else :
    print("Neither")
                     
