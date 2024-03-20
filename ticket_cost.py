import pandas



#currency formatting function 

def currency(x):
    return "${:.2f}".format(x)


# Dictionaries to hold ticket details
all_names = ["a", "b", "c", "d", "e"]
all_tickets_cost = ["7.50", "7.50", "10.50", "10.50", "6.50"]
surcharge = ["0", "0", "0.53", "0.53", "0"]

mini_movie_dict = {
    "name":all_names, 
    "ticket price": all_tickets_cost,
    "surcharge":surcharge 
} 

mini_movie_frame = pandas.DataFramey(mini_movie_dict)
print(mini_movie_frame)