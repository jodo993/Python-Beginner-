# This program prints a multiplication table

# Number range from 1 to 10
# i * j is row multiply with column for result
for i in range(1,11) :
    for j in range(1,11):
        print(i * j, end="\t")
    print()
