from fillinquestion import FillInQuestion

# Create the question and expected answer
question = FillInQuestion()
question.setText("The inventor of Python was _Guido van Rossum_")

# Display the question and obtain user's response
question.display()
response = input("Your answer: ")
print(question.checkAnswer(response))
