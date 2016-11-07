class SodaCan :
    def __init__(self, height, radius) :
        self._height = height
        self._radius = radius

    def getSurfaceArea(self) :
        return (2 * 3.14 * self._radius * self._height) + (2 * 3.14 * (self._radius*self._radius))

    def getVolume(self) :
        return 3.14 * (self._radius * self._radius) * self._height
        
