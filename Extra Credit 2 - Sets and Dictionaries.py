def main():

    # Create dictionary
    studentResult = {}

    # Present options
    print("Pick an option below.")
    print("Type 'A' to add students and grades.")
    print("Type 'R' to remove students and grades.")
    print("Type 'M' to modify grades.")
    print("Type 'P' to print results.")
    print("Type 'Q' to quit.")

    choice = input("Choice is: ").upper()   # Get choice
    
    while choice != "Q":
        # Add student and grade
        if choice == "A":
            print("Add names & grades. To end press 'Q'")
            studentName = input("Add name: ")
            studentGrade = input("Add grade: ").upper()
            while studentName and studentGrade != "Q":
                studentResult[studentName] = studentGrade
                studentName = input("Add name: ")
                studentGrade = input("Add grade: ").upper()
                
            print("Pick an option below.")
            choice = input("Choice is: ").upper()

        # Remove student and grade
        elif choice == "R":
            print("Remove names. To end press 'Q'")
            studentName = input("Remove who: ")
            studentResult.pop(studentName)
            while studentName != "Q":
                studentName = input("Remove who: ")
                if studentName != "Q":
                    studentResult.pop(studentName)
            print("Pick an option below.")
            choice = input("Choice is: ").upper()

        # If student name is found, change student and grade
        elif choice == "M":
            print("Which student grade to change? To end press 'Q'")
            studentName = input("Modify for who: ")
            if studentName in studentResult:
                print("Name found.")
                studentGrade = input("Change to what grade: ")
                studentResult[studentName] = studentGrade
            else:
                print("Name not found.")

            # Change grade
            while studentName != "Q":
                studentName = input("Modify for who: ")
                if studentName in studentResult:
                    print("Name found.")
                    studentGrade = input("Change to what grade: ").upper()
                    studentResult[studentName] = studentGrade
                else:
                    print("Name not found.")
            print("Pick an option below.")
            choice = input("Choice is: ").upper()

        # Print result
        elif choice == "P":
            print("Result is: ")
            # Print each student with grade
            for x in studentResult:
                print(x,":",studentResult[x])
            print("Pick an option below.")
            choice = input("Choice is: ").upper()
            
        else:
            print("Bye")

# Start program 
main()
