gradeCount = {"A": 8, "D": 3, "B": 15, "F": 2, "C": 6}

print("Keys:")
for key in gradeCount:
    print(key)

print("Values:")
valueList = []
for value in gradeCount.values():
    valueList.append(value)
    print(value)
print("All key & value pairs: ", gradeCount)
