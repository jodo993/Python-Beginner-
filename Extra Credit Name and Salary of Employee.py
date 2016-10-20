name = input("Enter name: ")
salary = float(input("Enter wage: "))
hours = float(input("Enter hours: "))

if hours <= 40.00:
    pay = salary * hours
elif hours > 40.00:
    overHours = hours - 40.00
    overSalary = salary * 1.5
    normalPay = 40.00 * salary
    overPay = overHours * overSalary
    pay = normalPay + overPay

print("Total pay is:", pay)
