from grade import Grade

class Student :

    # Set name and initialize quiz score and numbers to 0
    def __init__(self, studentName, grade = 0) :
        self._studentName = studentName
        self._gradeTotal = 0
        self._numberOfGrades = 0
        if grade == "A" :
            self._grade = 4
        elif grade == "A-" :
            self._grade = 3.7
        elif grade == "B+" :
            self._grade = 3.3
        elif grade == "B" :
            self._grade = 3.0
        elif grade == "B-" :
            self._grade = 2.7
        elif grade == "C+" :
            self._grade = 2.3
        elif grade == "C" :
            self._grade = 2.0
        elif grade == "C-" :
            self._grade = 1.7
        elif grade == "D+" :
            self._grade = 1.3
        elif grade == "D" :
            self._grade = 1.0
        elif grade == "D-" :
            self._grade = 0.7
        else :
            self._grade = 0
            
    def getName(self) :
        return self._studentName

    def addQuiz(self, grade) :
        self._gradeTotal = self._gradeTotal + self._grade.getScore()
        self._numberOfGrades = self._numberOfGrades + 1

    def getTotalScore(self) :
        return self._gradeTotal

    def getAverageScore(self) :     # Find average
        return self._gradeTotal / self._numberOfGrades
