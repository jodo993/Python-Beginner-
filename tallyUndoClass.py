class Tally :

    def __init__(self) :
        self._count = 0
        
    def reset(self) :
        self._value = 0

    def click(self) :
        self._value += 1
        self._count = self._count + 1
        
    def getValue(self) :
        return self._value

    def undo(self) :
        if self._count > 0 :
            self._value -= 1
            self._count = self._count - 1
        else :
            self._value = 0
