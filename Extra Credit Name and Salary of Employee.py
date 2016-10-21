# This program determines the pay wage of an employee depending on hours worked

name = input("Enter name: ")            # Ask for name
salary = float(input("Enter wage: "))   # Ask for wage
hours = float(input("Enter hours: "))   # Ask for hours worked

if hours <= 40.00:                      # If less than 40 hours, use this
    pay = salary * hours
elif hours > 40.00:                     # To find wage with overtime
    overHours = hours - 40.00           # Find number of overtime hours
    overSalary = salary * 1.5           # Find overtime wage
    normalPay = 40.00 * salary          # Find normal pay
    overPay = overHours * overSalary    # Find overtime pay
    pay = normalPay + overPay           # Total pay

print("Total pay is: $", pay)
