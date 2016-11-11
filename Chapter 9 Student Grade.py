# This program finds the total and average grade score of a student
from studentGrade import Student     # Get class Student from file
from grade import Grade
student = Grade("Bob")    # Create object student

# Add quiz grade
student.addQuiz(Grade("D"))
student.addQuiz(Grade("A-"))
student.addQuiz(Grade("B"))

# Display
print(student.getName(), "had a total of %.1f grade points" % student.getTotalScore())
print("The GPA was %.1f." % student.getAverageScore())
