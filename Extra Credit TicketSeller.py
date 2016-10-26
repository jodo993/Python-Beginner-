# This program sells ticket and will continue until there are no tickets left

tickets = 20    # Amount of tickets to be sold

print("There are currently ", tickets, "tickets remaining.")        # Prompt input
cinemaTickets = int(input("Enter how many tickets you want: "))

buyers = 0          # Keep track of buyers

# Sell tickets until there are no more tickets
while tickets > 0:
    if tickets - cinemaTickets >= 0:    # Makes sure that user can't buy negative tickets
        if cinemaTickets <= 4:
            tickets = tickets - cinemaTickets
            buyers = buyers + 1
            print("There are currently ", tickets, "tickets remaining.")
            if tickets > 0:         # Ask for purchase again if there are tickets left
                cinemaTickets = int(input("Enter how many tickets you want: "))
        else:
            print("You can only buy up to four.")
            cinemaTickets = int(input("Enter how many tickets you want: "))
    else:
        print("There are not enough tickets left.")
        print("There are currently ", tickets, "tickets remaining.")
        print("You can only buy up to four.")
        cinemaTickets = int(input("Enter how many tickets you want: "))
        
print("The total number of buyers was", buyers)
