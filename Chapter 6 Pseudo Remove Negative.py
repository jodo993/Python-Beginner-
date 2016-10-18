create = [1, 2, -8, 5, -9, 6]

for i in range(0, len(create)):
    if create[i] < 0:
        create.pop(i)
        create.insert(i, " ")

print(create)

# Create list and remove all negative numbers and keep position the same
