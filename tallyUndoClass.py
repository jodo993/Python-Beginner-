class Tally :

    def __init__(self) :
        self._count = 0     # Keeps track of how many clicks
        
    def reset(self) :
        self._value = 0     # Reset click to 0

    def click(self) :
        self._value += 1    # Add one to click
        self._count = self._count + 1   # Add one to count
        
    def getValue(self) :    # Return number of clicks
        return self._value

    # If above 0, subtract one, else 
    def undo(self) :
        if self._count > 0 :
            self._value -= 1
            self._count = self._count - 1
        else :
            self._value = 0
