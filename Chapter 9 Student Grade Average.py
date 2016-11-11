# This program finds the total and average quiz score of a student
from studentGradeAverage import Student     # Get class Student from file

student = Student("Bob")    # Create object student

# Add quiz scores
student.addQuiz(50)
student.addQuiz(90)
student.addQuiz(75)

# Display
print(student.getName(), "had a total score of %.2f." % student.getTotalScore())
print("The average score was %.1f." % student.getAverageScore())
