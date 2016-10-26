# This program calculate the amount of financial assistance for families
def main():

    print("Enter required information or -1 to quit.")
    income = float(input("Please enter your income: "))
    children = float(input("Please enter number of children: "))

    # If input is valid, call method
    if income > 0 and children > 0:
        computeAssistance(income, children)
    else:
        print("Thank you. See you later.")

#@param income - income of family
#@param children - number of kids
#@param return - how much assistance the family got
def computeAssistance(income, children):

    tierOne = 1000          # Assistance for 30-39k
    tierTwo = 1500          # Assistance for 20-29k
    tierThree = 2000        # Assistance for sub 20k

    # Determines which program the family falls under
    if income >= 30000 and income <= 39999:
        if children >= 3:
            financialAssistance = children * tierOne
        else:
            return print("Sorry you do not qualify.")
    elif income >= 20000 and income <= 29999:
        if children >= 2:
            financialAssistance = children * tierTwo
        else:
            return print("Sorry you do not qualify.")
    elif income < 20000:
        financialAssistance = children * tierThree
    else:
        return print("Sorry your income is too high.")
    
    return print("Your financial assistance amount is: $ %.2f"% financialAssistance)    

# Start program
main()

