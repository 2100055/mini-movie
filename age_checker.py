#Functions go here 

# Checks users enter an integer to a given question

def number_check(question):

    while True:

        try:
            response = int(input(question))
            return response


        except ValueError:
            print( "please enter an integer")

# Main routine goes here 
tickets_sold = 0

while True:

    name = input("please enter your name / xxx to quit: ")
    
    if name == 'xxx':
        break

    age = number_check("Age: ")

    if 12 <= age <= 120:
        pass

    elif age < 12:
        print("Sorry, you are too young for this movie ")
        continue
    else:
        print("??  that looks like a typo, please try again")
        
        continue

    tickets_sold += 1