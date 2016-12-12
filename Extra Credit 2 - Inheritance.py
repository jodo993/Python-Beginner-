from classQuestion import MultiChoiceQuestion

def main():
    
    question = MultiChoiceQuestion()
    question.setText("Of Apple, Tomato, Carrot, Cucumber and Celery, list all that are fruit.")
    question.setAnswer("Apple Tomato")

    question.display()
    response = input("Your answer: ")
    print(question.checkAnswer(response))
    
main()
