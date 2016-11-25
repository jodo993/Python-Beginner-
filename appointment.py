class Appointment:

    def __init__(self, day, month, year, description):
        self._description = description
        self._date = date(day,month,year)

    def occursOn(self, day, month, year):
        if self._date = date(day,month,year)
            return True
        else:
            return False    

class Onetime(Appointment):
    
    def __init__(self, day, month, year, description):
        super(OneTime, self).__init__(day, month, year, description)

    def occursOn(date):
        return true;

class Daily(Appointment):

    def __init__(self, day, month, year, description):
        super(Daily, self).__init__(day, month, year, description)

    def occursOn(date):
        return true;

class Monthly(Appointment):

    def __init__(self,day,month,year,description):
       super(Monthly,self).__init__(day,month,year,description)

    def occursOn(date):
        return true;

def occursOn(year, month, day):

     if self._date == day:
           return True
       else:
           return False
