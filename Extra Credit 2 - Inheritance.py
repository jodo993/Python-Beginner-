# This program allow multiple answers for a question
# Import class
from classQuestion import MultiChoiceQuestion

def main():

    # Create question object and set answers and question
    question = MultiChoiceQuestion()
    question.setText("Of Apple, Tomato, Carrot, Cucumber and Celery, list all that are fruit.")
    question.setAnswer("Apple Tomato")

    # Display questions and get response and check
    question.display()
    response = input("Your answer: ")
    print(question.checkAnswer(response))

# Start program
main()
