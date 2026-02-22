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
    
    print("-- Displaying Menu --\n1. Display Roster\n2. Add Crew\n3. Remove Crew\n4. Update Rank\n5. Exit")

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

def add_member(names, ranks, divs, ids):
    while True:
        try:
            new_ids = int(input("Insert new member ID: "))
        except ValueError:
            print("ID's are integers. Try again.")
        else:
            if new_ids in ids:
                print("ID is already taken. Try again.")
            else:
                print("ID is unique")
                ids.append(new_ids)
                break

    valid_rank = ["Fleet Admiral", "Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Officer", "Cadet"]
    valid_divs = ["Command", "Science", "Operations", "Security", "Medical", "Engineering"]
    
    new_name = input("Enter the new member's name: ")
    names.append(new_name)

    while True:
        new_rank = input("Enter their Rank: ")
        if new_rank in valid_rank:
            print("Rank added.")
            ranks.append(new_rank)
            break
        else:
            print("That is not a Rank.")

    while True:
        new_divs = input("Enter their Division: ")
        if new_divs in valid_divs:
            print("Division added.")
            divs.append(new_divs)
            break
        else:
            print("That is not a Division.")

    print("Crew Member has been added to the ship database.")

def remove_member(names, ranks, divs, ids):
    while True:
        try:
            remove_id = int(input("Enter ID of Crew Member to be removed: "))
        except ValueError:
            print("IDs can only be Integers.")
        else:
            if remove_id in ids:
                index = ids.index(remove_id)
                remove_name = names[index]

                names.pop(index)
                ranks.pop(index)
                divs.pop(index)
                ids.pop(index)

                print("Crew Member has been removed")
                return names, ranks, divs, ids
            
            else:
                print("No Crew Member exists with that ID. Try again.")

def update_rank(names, ranks, ids):
    while True:
        try:
            update_id = int(input("Enter the ID of the Crew Member whose Rank will be updated."))
        except ValueError:
            print("IDs can only be Integers.")
        else:
            if update_id in ids:
                print("ID verified.")
                break
            else:
                print("There is no current Crew Member with that Rank.")
                continue
    
    index = ids.index(update_id)
    current_name = names[index]
    current_rank = ranks[index]
    valid_rank = ["Fleet Admiral", "Admiral", "Captain", "Commander", "Lieutenant Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Officer", "Cadet"]
    while True:
        new_rank = input("Enter new rank: ")
        if new_rank in valid_rank:
            ranks[index] = new_rank
            print(f"{current_name} has been updated from {current_rank} to {new_rank}.")
            break
        else:
            print("That is not a Rank. Try again.")
    
    return names, ranks, ids
    


def main():
    names, ranks, divs, ids = init_database() #Sets up lists at the start
    option = display_menu(names) #Receives option from display
    if option == 1:
        print("Option 1 not yet available.")#placeholder
    elif option == 2:
        names, ranks, divs, ids = add_member(names, ranks, divs, ids)
    elif option == 3:
        names, ranks, divs, ids = remove_member(names, ranks, divs, ids)
    elif option == 4:
        names, ranks, ids = update_rank(names, ranks, ids)
    


main()