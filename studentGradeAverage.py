class Student :

    # Set name and initialize quiz score and numbers to 0
    def __init__(self, studentName) :
        self._studentName = studentName
        self._quizScore = 0
        self._numberOfQuiz = 0

    def getName(self) :
        return self._studentName

    def addQuiz(self, score) :
        self._quizScore = self._quizScore + score   # Add to quiz score total
        self._numberOfQuiz = self._numberOfQuiz + 1 # Increment quiz # by 1

    def getTotalScore(self) :
        return self._quizScore

    def getAverageScore(self) :     # Find average
        return self._quizScore / self._numberOfQuiz
