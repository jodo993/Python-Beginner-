# This program validates a user password and determines if it meets the
# requirements of 1 upper, 1 lower, and a number.
def main():

    # Ask for user input
    print("Enter a password that is 8 characters long, contains 1 uppercase, 1 lowercase, and 1 number.")
    password = input("Enter password: ")
    passCheck = input("Re-enter password: ")
    
    condition = isValid(password)

    # Checks to see if both entries is the same and if password is invalid, reprompt
    while password != passCheck and isValid(password) == False:
        print("Invalid try again.")
        password = input("Enter password: ")
        passCheck = input("Re-enter password: ")
        
    if isValid(password):
        print("Password is good.")
    else:
        print("No good")

#@param password - holds user password
#@return - true if password pass or false if password fails test
def isValid(password):
    if len(password) < 8:
        return False
    else: # Checks to see if at least one of each is in the password
        for i in password:
            if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                for j in password:
                    if j in "abcdefghijklmnopqrstuvwyz":
                        for k in password:
                            if k in "0123456789":
                                return True

# Start program
main()
