def main():
    
    print("Enter a password that is 8 characters long, have one uppercase, lowercase, and digit.")
    password = input("Please enter a password: ")
    passCheck = input("Please re-enter password: ")

    same = True
    while same:
        if len(password) >= 8 and len(passCheck) >= 8:
            if password == passCheck:
                same = False
                isValidPassword(password)
            else:
                password = input("Please enter a password: ")
                passCheck = input("Please re-enter password: ")
        else:
            password = input("Please enter a password: ")
            passCheck = input("Please re-enter password: ")
    
def isValidPassword(password):

    valid = False
    for char in password:
        if char in "alex":
            password = password.replace(char, 'i')
            valid = True
            return print(password)
        else:
            return print("hert")
                
main()
