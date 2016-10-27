print("Enter a set of floating point numbers.")
numbers = float(input(""))

ok = True
total = 0.0
tries = 2

while tries > 0:
    try:
        if ok:
            total = total + numbers
        else:
            tries = tries - 1
            numbers = float(input(""))
            
                
        
        
