def init_database(): #Presets for the intital lists
    names = ["Picard", "Riker", "Data", "Worf", "Spock"]
    ranks = ["Captain", "Commander", "Lt.Commander", "Lieutenant", "Commander"]
    divs = ["Command", "Command", "Operations", "Security", "Science"]
    ids = [1, 2, 3, 4, 5]
    return names, ranks, divs, ids

def display_menu(names):
    user = str(input("Enter full name: "))
    if user in names: #Testing Input Validation and parsing lists.
        print(f"Welcome, {user}.")
    else:
        print(f"Logged in as: {user}")
    
    print("-- Displaying Menu --\n1. Display Roster\n2. Add Crew\n3. Remove Crew\n4. Update Rank\n5. Search Crew\n6. Crew Payroll\n7. Count Officers\n8. Exit")

    while True:
        try: #Try-catching for Integer Input.
            option = int(input("Please select an option: "))
        except ValueError:
            print("Not an Integer. Try again.")
        else:
            if option < 1 or option > 8: #Checks if it is within choice range.
                print("That was not an option. Try again.")
                continue
            else:
                return option

def add_member(names, ranks, divs, ids):
    while True:
        try: #Catches non-integer inputs and ID's below 1.
            new_ids = int(input("Insert new member ID: "))
        except ValueError:
            print("ID's are integers.")
        else:
            if new_ids in ids:
                print("ID is already taken. Try again.")
            elif new_ids < 1:
                print("ID's can't be negative.")
            else:
                print("ID is unique")
                ids.append(new_ids) #Before adding it to the end of the list.
                break
    #Set list of the different Ranks and Divisions in TNG.
    valid_rank = ["Fleet Admiral", "Admiral", "Captain", "Commander", "Lt.Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Officer", "Cadet"]
    valid_divs = ["Command", "Science", "Operations", "Security", "Medical", "Engineering"]
    
    new_name = input("Enter the new member's name: ")
    names.append(new_name) #Adds the new name to the end of the list.

    while True:
        new_rank = input("Enter their Rank: ")
        if new_rank in valid_rank: #Checks if the Rank is a valid one.
            print("Rank added.")
            ranks.append(new_rank) #Before adding it to the end of the list.
            break
        else:
            print("That is not a Rank.")

    while True:
        new_divs = input("Enter their Division: ")
        if new_divs in valid_divs: #Checks if the Division is a valid one.
            print("Division added.")
            divs.append(new_divs) #Before adding it to the end of the list.
            break
        else:
            print("That is not a Division.")

    print("Crew Member has been added to the ship database.")
    return names, ranks, divs, ids #returns the vesrions of the lists with the new indexed Crew Member.

def remove_member(names, ranks, divs, ids):
    while True:
        try: #Try-catching for the correct input. Checking for a negative number input doesn't matter as there already cant be one in the system, so it would return the same result.
            remove_id = int(input("Enter ID of Crew Member to be removed: "))
        except ValueError:
            print("IDs can only be Integers.")
        else: #If there's no error:
            if remove_id in ids: #Checks to see whether the input ID is in the list.
                index = ids.index(remove_id) #Finds that ID's index number

                names.pop(index) #Removes everything with the same index number from each of the lists.
                ranks.pop(index)
                divs.pop(index)
                ids.pop(index)

                print("Crew Member has been removed.")
                return names, ranks, divs, ids #Returns the updated lists.
            
            else:
                print("No Crew Member exists with that ID. Try again.")

def update_rank(names, ranks, ids):
    while True:
        try: #Try catch for the correct input.
            update_id = int(input("Enter the ID of the Crew Member whose Rank will be updated: "))
        except ValueError:
            print("IDs can only be Integers.")
        else:
            if update_id in ids: #If the ID is in the list, it's valid.
                print("ID verified.")
                break
            else: #If not, the loop continues.
                print("There is no current Crew Member with that Rank.")
                continue
    
    index = ids.index(update_id) #Uses the current ID to find the index.
    current_name = names[index] #Uses the index to find the name and rank of the Crew Member.
    current_rank = ranks[index]
    valid_rank = ["Fleet Admiral", "Admiral", "Captain", "Commander", "Lt.Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Officer", "Cadet"]
    while True:
        new_rank = input("Enter new rank: ")
        if new_rank in valid_rank: #Checks the Rank against the valid Ranks.
            ranks[index] = new_rank
            print(f"{current_name} has been updated from {current_rank} to {new_rank}.")
            break
        else:
            print("That is not a Rank. Try again.")
    
    return names, ranks, ids #returns the lists used, with ranks being the only one that really needs updating.
    
def display_roster(names, ranks, divs, ids):
    print(f"{'ID'} | {'Name'} |   {'Rank'}   |  {'Division'}") #Rough spaces for each header.
    print("-"*41) #Title break.
    for i in range(len(names)): #For each item in the first list:
        print(f"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}") #print out each corrosponding item of the same index.

def search_crew(names, ranks, divs, ids):
    while True:
        search_term = input("Enter name to search for: ").lower()
        found = False
        print("Search Results")
        print("-"*14) #Title break.
        for i in range(len(names)): #For each item in names:
            if search_term in names[i].lower(): #Check the characters in search_term against the string of each name.
                print(f"{ids[i]} - {names[i]} - {ranks[i]} - {divs[i]}")
                found = True

        if found == False:
            print(f"Could not find anyone with {search_term} in their name.")
        break #Kicks you back out to the search options.


def filter_by_division(names, divs):
    found = False
    while found == False:
        search_divs = input("What Division are you looking for?: ")
        match search_divs: #Matches the search:
            case "Command" | "Science" | "Operations" | "Security" | "Medical" | "Engineering": #Against the recognised Divisions.
                print("Search Results")
                print("-"*14)
                for i in range(len(names)): #For each item in a list:
                    if search_divs == divs[i]: #Check each item for the searched Division.
                        print(names[i]) #Print if one is found.
                        found = True #If even one is found, flip the found Boolean.
                
                if found == False:
                    print("No crew members found in that division.") #If none are found by the end.
                    break #Kicks you back into the search options.
            
            case _: #If it isn't a recognised Division, reject it.
                print("That is not a Division. Try again.")

def calculate_payroll(ranks):
    costs = [3000, 2500, 2000, 1500, 1000, 750, 500, 400, 200, 100] #Base costs, aligning with the same index's from the valid_rank list.
    valid_rank = ["Fleet Admiral", "Admiral", "Captain", "Commander", "Lt.Commander", "Lieutenant", "Lieutenant Junior Grade", "Ensign", "Officer", "Cadet"]
    total_cost = 0
    for rank in ranks: #For each Rank in our list:
        if rank in valid_rank: #Compare it to the valid Ranks list, then use the same index to figure out the costs.
            index = valid_rank.index(rank)
            total_cost += costs[index]
            print(rank, costs[index]) #This was for testing, just to print each individual cost along with it's Rank to double check.
    print(f"The total cost of the crew is {total_cost}.")

def count_officers(ranks):
    count = 0
    ad_count = 0
    for rank in ranks:
        if rank == "Captain" or rank == "Commander": 
            count += 1
        elif rank == "Fleet Admiral" or rank == "Admiral": #Since I added ranks higher than captian, I added a seperate count for them too.
            ad_count += 1
    print(f"Captain or Commander Officers: {count}\nTotal Admirals: {ad_count}")

def main():
    names, ranks, divs, ids = init_database() #Sets up lists at the start
    while True:
        option = display_menu(names) #Receives option from display
        if option == 1:
            display_roster(names, ranks, divs, ids)
        elif option == 2:
            names, ranks, divs, ids = add_member(names, ranks, divs, ids)
        elif option == 3:
            names, ranks, divs, ids = remove_member(names, ranks, divs, ids)
        elif option == 4:
            names, ranks, ids = update_rank(names, ranks, ids)
        elif option == 5:
            print("Search Options:\n1. Search by Name\n2. Filter by Division\n3. Exit")
            while True:
                choice = input("Please select an option: ") #Goes to the choice menu.
                if choice == "1":
                    search_crew(names, ranks, divs, ids)
                    print("Search Options:\n1. Search by Name\n2. Filter by Division\n3. Exit")
                elif choice == "2":
                    filter_by_division(names, divs)
                    print("Search Options:\n1. Search by Name\n2. Filter by Division\n3. Exit")
                elif choice == "3":
                    print("Exiting...")
                    break #Exits just the choice menu.
                else:
                    print("Not an option. Try again.")
        elif option == 6:
            calculate_payroll(ranks)
        elif option == 7:
            count_officers(ranks)
        elif option == 8:
            break #Exits the loop keeping the program running.
        else:
            print("That was not an option. Try again.") #For if the option wasn't valid.
        print("-"*41) #Separates each time the main menu is presented again.
main()