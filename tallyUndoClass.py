class Tally :

    def reset(self) :
        self._value = 0

    def click(self) :
        count = count + 1
        self._value += 1
        
    def getValue(self) :
        return self._value

    def undo(self) :
        if count > 0 :
            self._value -= 1
