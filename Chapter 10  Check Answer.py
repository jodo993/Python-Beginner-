from questions import Question

# Create ques
question = Question()

# Create question and answer
question.setQuestion("Who is the inventor of Python?")
question.setAnswer("Guido van Rossum")

# Display question and obtain user's response
question.display()
response = input("Your answer: ")
#question.modifiedAnswer(response)
print(question.checkAnswer(response))

