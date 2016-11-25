class Question:

    def __init__(self):
        self._text = ""
        self._answer = ""

    def setText(self, questionText):
        self._text = questionText

    def setAnswer(self, correctResponse):
        self._answer = correctResponse

    # Compare question and answer
    def checkAnswer(self, response):
        if response == self._answer:
            return self._text.replace("_____", "Guido van Rossum")
        else:
            return False

    def display(self):
        print(self._text)

class FillInQuestion(Question):

    def __init__(self):
        super().__init__()

    # Set question and answer
    def setText(self, questionText):
        self._correctResponse = questionText.replace("Guido van Rossum", "_____")
        super().setText(self._correctResponse)
        super().setAnswer("Guido van Rossum")

    def display(self):
        super().display()
