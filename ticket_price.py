# Calculate the ticket price based on age
def calc_ticket_price(var_age):
    
    # Ticket is $7.50 for users under 16
    if  var_age < 16:
        price = 7.5

    #ticket is $10.50 for users between 16 and 64
    elif var_age < 65:
        price = 10.5

    # ticket price is $6.50 for seniors (65+)
        
    else:
        price = 6.5

    return price
   
# Loop for testing...
while True:

    # Get age (assume user put a valid integer)
    age = int(input(" Age: "))

    # Calculate ticket cost 
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, Ticket price: ${:.2f}".format(age, ticket_cost))