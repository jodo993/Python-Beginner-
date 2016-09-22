# This program determines which time is earlier

# Asks for hours and minutes
firstHour = int(input("Please enter first hour: "))
firstMinute = int(input("Please enter first minute: "))
secondHour = int(input("Please enter second hour: "))
secondMinute = int(input("Please enter second minute: "))

if firstHour < secondHour :
    print("First time comes first.")
elif firstHour == secondHour :
    if firstMinute < secondMinute :
        print("First time comes first.")
    elif firstMinute == secondMinute :
        print("Both times are the same.")
    else :
        print("Second time comes first.")
else :
    print("Second time comes first.")
