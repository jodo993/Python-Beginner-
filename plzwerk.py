def main():

    studentResult = {}

    print("Pick an option below.")
    print("Type 'A' to add students and grades.")
    print("Type 'R' to remove students and grades.")
    print("Type 'M' to modify grades.")
    print("Type 'P' to print results.")
    print("Type 'Q' to quit.")

    choice = input("Choice is: ").upper()
    
    while choice != "Q":
        if choice == "A":
            print("Add names & grades. To end press 'Q'")
            studentName = input("Add name: ")
            studentGrade = input("Add grade: ")
            while studentName and studentGrade != "Q":
                studentResult[studentName] = studentGrade
                studentName = input("Add name: ")
                studentGrade = input("Add grade: ")
                
            print("Pick an option below.")
            choice = input("Choice is: ").upper()
            
        elif choice == "R":
            print("Remove names. To end press 'Q'")
            studentName = input("Remove who: ")
            studentResult.pop(studentName)
            while studentName != "Q":
                studentName = input("Remove who: ")
                studentResult.pop(studentName)
            print("Pick an option below.")
            choice = input("Choice is: ").upper()
        
        elif choice == "M":
            print("Which student grade to change? To end press 'Q'")
            studentName = input("Modify for who: ")
            if studentName in studentResult:
                print("Name found.")
                studentGrade = input("Change to what grade: ")
                studentResult[studentName] = studentGrade
            else:
                print("Name not found.")
            
            while studentName != "Q":
                studentName = input("Modify for who: ")
                if studentName in studentResult:
                    print("Name found.")
                    studentGrade = input("Change to what grade: ")
                    studentResult[studentName] = studentGrade
                else:
                    print("Name not found.")
            print("Pick an option below.")
            choice = input("Choice is: ").upper()
                
        elif choice == "P":
            print("Result is: ")
            for x in studentResult:
                print(x,":",studentResult[x])
            print("Pick an option below.")
            choice = input("Choice is: ").upper()
        else:
            print("Bye")

            
main()
