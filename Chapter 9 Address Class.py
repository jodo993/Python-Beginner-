# This program takes the address information and display then see which one comes first
from address import Address

# Create address objects
addressOne = Address(2500, "University Drive", "Some City", "Some State", "12345")
addressTwo = Address(1200, "College Blvd", "Other City", "Other State", "99102", "12")

# Get the address and display it
addressOneResult = addressOne.printt()
addressTwoResult = addressTwo.printt()
print(addressOneResult)
print(addressTwoResult)

# Finds out with address comes first based on postal code
comesBeforeResult = addressOne.comesBefore(addressTwo)
print(comesBeforeResult)
