name = input("enter name")

total = 0.0
count = 0.0
score = float(input("enter score"))
while score > 0 :
    total = total + score
    count = count + 1
    score = float(input("enter score"))

if count > 0 :                  
    average = total / count

print("Name is: ", name)
print("average is ", average)
    

