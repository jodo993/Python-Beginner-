class Address :
        
    def __init__(self, houseNumber, street, city, state, postalCode, apartmentNumber = "") :
        self._houseNumber = houseNumber
        self._street = street
        self._city = city
        self._state = state
        self._postalCode = postalCode
        self._apartmentNumber = apartmentNumber

    def printt(self) :
        print(self._street)
        print(self._city, self._state, self._postalCode)

    def comesBefore(self, other) :
        if self._postalCode < other._postalCode :
            return print("Address 1 comes first.")
