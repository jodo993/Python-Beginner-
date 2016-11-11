class Grade :

    def __init__(self, grade) :
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

    def getScore(self) :
        return self._grade
