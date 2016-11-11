from address import Address

addressOne = Address(2500, "University Drive", "Some City", "Some State", "12345")
addressTwo = Address(1200, "College Blvd", "Other City", "Other State", "99102", "12")

addressOneResult = addressOne.printt()
addressTwoResult = addressTwo.printt()
print(addressOneResult)
print(addressTwoResult)

comesBeforeResult = addressOne.comesBefore(addressTwo)
print(comesBeforeResult)
