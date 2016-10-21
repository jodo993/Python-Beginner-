
def main():

    print("Enter required information or -1 to quit.")
    income = float(input("Please enter your income: "))
    children = float(input("Please enter number of children: "))

    if income > 0 and children > 0:
        computeAssistance(income, children)
    else:
        print("Thank you. See you later.")

def computeAssistance(income, children):

    tierOne = 1000
    tierTwo = 1500
    tierThree = 2000
    
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

main()

