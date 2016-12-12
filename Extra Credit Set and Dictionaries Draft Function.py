def main():

    studentResult = {}

    choice = menu()
    
    if choice == "A":
        studentResult = add(studentResult)
        menu()
    elif choice == "R":
        studentResult = remove(studentResult)
        menu()
    elif choice == "M":
        studentResult = modify(studentResult)
        menu()
    elif choice == "P":
        studentResult = display(studentResult)
        menu()
    else:
        print("Goodbye.")

def menu():
    
    print("Pick an option below.")
    print("Type 'A' to add students and grades.")
    print("Type 'R' to remove students and grades.")
    print("Type 'M' to modify grades.")
    print("Type 'P' to print results.")
    print("Type 'Q' to quit.")

    choice = input("Choice is: ").upper()
    return choice

def add(studentResult):
    
    print("Add names & grades. To end press 'Q'")
    studentName = input("Add name: ")
    studentGrade = input("Add grade: ")
    studentResult[studentName] = studentGrade
    while studentName and studentGrade != "Q":
        studentName = input("Add name: ")
        studentGrade = input("Add grade: ")
        studentResult[studentName] = studentGrade

    return studentResult

def remove(studentResult):

    print("Remove names. To end press 'Q'")
    studentName = input("Remove who: ")
    studentResult.pop(studentName)
    while studentName != "Q":
        studentName = input("Remove who: ")
        studentResult.pop(studentName)

    return studentResult

def modify(studentResult):

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

    return studentResult

def display(studentResult):
    
    for x in studentResult:
        return print(x, studentResult[x])
            
main()
