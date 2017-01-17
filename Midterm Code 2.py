print("Enter a score for the grade or -1 to quit.")
score = int(input("Score is: "))
while score >= 0:
    if score >= 0:
        if score >= 90 and score <= 100:
            grade = "A"
        elif score >= 80 and score <= 89:
            grade = "B"
        elif score >= 70 and score <= 79:
            grade = "C"
        elif score >= 60 and score <= 69:
            grade = "D"
        elif score < 60:
            grade = "F"
        else:
            print("Not valid. Restart.")
    print("The letter grade for that score is ", grade)
    print("Enter a score for the grade or -1 to quit.")
    score = int(input("Score is: "))



