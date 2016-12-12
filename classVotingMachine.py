class VotingMachine:

    # Initial votes to 0
    def __init__(self):
        self._democrat = 0
        self._republican = 0

    # Return votes for Democrat s   
    def getTalliesD(self):
        return self._democrat

    # Return votes for Republicans
    def getTalliesR(self):
        return self._republican

    # Add one vote per call
    def voteDemocrat(self):
        self._democrat = self._democrat + 1

    # Add one vote per call
    def voteRepublican(self):
        self._republican = self._republican + 1

    # Set vote to 0
    def clear(self):
        self._value = 0

    
    
