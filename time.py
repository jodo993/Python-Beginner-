from classTime import Time

def main():

    time = Time(9,0)
    print("Current time: ", time.printTime())
    time.reset()
    print("Reset Time: ", time.printTime())
    time.addMinute(3)
    print("Add 3 minutes: ", time.printTime())
    
main()
