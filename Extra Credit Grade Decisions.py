# This program accepts a letter grade and determines its numeric value

# Prompt user input
grade = input("Please enter a letter grade: ").upper()

# Assign values to grade
EXTRA = 0.3
A = 4
B = 3
C = 2
D = 1
F = 0

# Determines the requirements and display result
if grade == "A+" or grade == "A":
    grade = A
elif grade == "A-":
    grade = A - EXTRA
elif grade == "B+":
    grade = B + EXTRA
elif grade == "B":
    grade = B
elif grade == "B-":
    grade = B - EXTRA
elif grade == "C+":
    grade = C + EXTRA
elif grade == "C":
    grade = C
elif grade == "C-":
    grade = C - EXTRA
elif grade == "D+":
    grade = D + EXTRA
elif grade == "D":
    grade = D
elif grade == "D-":
    grade = D - EXTRA
else:
    grade = F
print("The numeric value is", grade)    # Display result
    
