class Tally :

    def __init__(self) :
        self._count = 0
        
    def setlimit(self, maximum) :
        self._maximum = maximum
        
    def reset(self) :
        self._value = 0

    def click(self) :
        self._value = self._value + 1
        self._count = self._count + 1

    def getValue(self) :
        if self._count <= self._maximum :
            return self._value
        else :
            return print("Limit exceeded")

            
        
