class Time:
    def __init__(self,hour,minute):
        self._hour = hour
        self._minute = minute

    def addMinute(self, minutes):
        self._minute = self._minute + minutes
        if self._minute > 59:
            while self._minute > 59:
               self._minute = self._minute - 60
               self._hour = self._hour + 1

    def reset(self):
        self._hour = 0
        self._minute = 0

    def printTime(self):
        return "%.2d:%.2d" % (self._hour,self._minute)
