class Question():

    # Initialize
    def __init__(self):
        self._question = ""
        self._answer = ""

    # Set the question
    def setQuestion(self, questionText):
        self._question = questionText

    # Set the answer to the question
    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    # Compare answer and user input
    def checkAnswer(self, response):
        return self._answer.lower().replace(" ", "") == response.lower().replace(" ", "")

    def display(self):
        print(self._question)

    # Change to lower case and no spaces
    #def modifiedAnswer(self, response):
        #self._response = response.strip()
        #self._response = response.lower()
