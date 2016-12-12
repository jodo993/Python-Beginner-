class VotingMachine:

    def __init__(self):
        self._democrat = 0
        self._republican = 0
        
    def getTalliesD(self):
        return self._democrat

    def getTalliesR(self):
        return self._republican

    def voteDemocrat(self):
        self._democrat = self._democrat + 1

    def voteRepublican(self):
        self._republican = self._republican + 1

    def clear(self):
        self._value = 0

    
    
