class Address :

    # Initialize house, street, city, state, zip, and apt #
    def __init__(self, houseNumber, street, city, state, postalCode, apartmentNumber = "") :
        self._houseNumber = houseNumber
        self._street = street
        self._city = city
        self._state = state
        self._postalCode = postalCode
        self._apartmentNumber = apartmentNumber

    # Print the address on two lines
    def printt(self) :
        print (self._street) 
        print (self._city, self._state, self._postalCode)

    # Compares which one comes first
    def comesBefore(self, other) :
        if self._postalCode < other._postalCode :
            return ("Address 1 comes first.")
