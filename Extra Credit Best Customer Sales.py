# This program creates an array of customers and sales and find the highest
# spending customer

def main():

    customers = []      # Create empty customer list
    sales = []          # Create empty sales list

    # Prompt first user input
    name = input("Enter customer: ")
    amount = float(input("Enter sales: "))

    # While sales is not 0, continue to ask for name and amount
    while amount != 0:
        customers.append(name)
        sales.append(amount)
        name = input("Enter customer: ")
        amount = float(input("Enter sales: "))

    nameOfBestCustomer(customers, sales)        # Calls function

#@param customers - list of customer names
#@param sales - list of sales amount
#@return - display best customer
def nameOfBestCustomer(customers, sales):

    # Initially set sub of zero as largest and best
    largestSale = sales[0]
    bestCustomer = customers[0]

    # Loops through array and when highest sale found, same index use for customer
    for i in range(1, len(sales)):
        if sales[i] > largestSale:
            largestSale = sales[i]
            bestCustomer = customers[i]
            return print("The best customer is: ", customers[i])
        
# Start program        
main()
