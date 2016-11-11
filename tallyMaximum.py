class Tally :

    def __init__(self) :
        self._count = 0     # Track clicks
        
    def setlimit(self, maximum) :   # Set limit
        self._maximum = maximum
        
    def reset(self) :
        self._value = 0

    def click(self) :
        self._value = self._value + 1   # Add to count and current value
        self._count = self._count + 1

    # Check if max is reached, if so, display limit
    def getValue(self) :
        if self._count <= self._maximum :
            return self._value
        else :
            return ("Limit exceeded")

            
        
