class MultiChoiceQuestion:

    # Initialize question and answer
    def __init__(self):
        self._text = ""
        self._answer = ""

    # Get the question
    def setText(self, questionText):
        self._text = questionText

    # Get the answer
    def setAnswer(self, answerText):
        self._answer = answerText

    # Compare response to answer, if match, true
    def checkAnswer(self, response):
        response = response.lower()
        response = response.split()
        self._answer = self._answer.lower()
        self._answer = self._answer.split()
        if response[0] == self._answer[0] and response[1] == self._answer[1]:  
            return True
        elif response[0] == self._answer[1] and response[1] == self._answer[0]:
            return True
        else:
            return False

    # Display question
    def display(self):
        print(self._text)
