def init_database():
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Science"]
    ids = [1, 2, 3, 4, 5]
    return names, ranks, divs, ids

def display_menu(names):
    user = str(input("Enter full name: "))
    if user in names: #Testing Input Validation
        print(f"Welcome, {user}.")
    else:
        print(f"Logged in as: {user}")
    
    print("-- Displaying Menu --\n1. Display Roster\n2. Add Crew\n3. Remove Crew\n4. Search Crew\n5. Exit")

    while True:
        try:
            option = int(input("Please select an option: "))
        except ValueError:
            print("Not an Integer. Try again.")
        else:
            if option < 1 or option > 5:
                print("That was not an option. Try again.")
                continue
            else:
                return option

def main():
    names, ranks, divs, ids = init_database() #Sets up lists at the start
    option = display_menu(names) #Receives option from display


main()