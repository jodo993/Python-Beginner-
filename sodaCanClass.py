class SodaCan :
    def __init__(self, height, radius) :    # Define height and radius of can
        self._height = height
        self._radius = radius

    # Get the surface area
    def getSurfaceArea(self) :
        return (2 * 3.14 * self._radius * self._height) + (2 * 3.14 * (self._radius*self._radius))

    # Get the volume
    def getVolume(self) :
        return 3.14 * (self._radius * self._radius) * self._height
        
