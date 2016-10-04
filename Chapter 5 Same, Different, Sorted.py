def main():
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    z = int(input("Enter a number: "))
    allTheSame(x,y,z)
    allDifferent(x,y,z)
    sort(x,y,z)

def allTheSame(x,y,z):
    if x == y & x == z :
        return print("True")
    else :
        print("False")

def allDifferent(x,y,z):
    if x != y & x != z & y != z :
        return print("True")
    else :
        return print("False")

def sort(x,y,z) :
    if x < y and x < z and y < z :
        return print("True")
    else :
        return print("False")
    
main() 
