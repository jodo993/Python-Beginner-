class Question():

    def __init__(self):
        self._question = ""
        self._answer = ""

    def setQuestion(self, questionText):
        self._question = questionText

    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    def checkAnswer(self, response):
        return self._response == self._answer

    def display(self):
        print(self._question)

    def modifiedAnswer(self, response):
        self._response = response.strip()
        self._response = self._response.lower()
        self._answer = self._answer.strip()
        self._answer = self._answer.lower()
        
        
    
