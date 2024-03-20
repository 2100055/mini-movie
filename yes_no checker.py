# Functions go here
def Yes_No(question):
    
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        
        elif response == 'no' or response == 'n':
            return 'no'
        
        else:
            print('please enter yes or no')

# Main routine goes here 
while True:
    want_instructions = Yes_No('Do you want instructions? ')

    if want_instructions == 'yes':
      print('Instructions go here')

    print('Program continues...')
    print()
