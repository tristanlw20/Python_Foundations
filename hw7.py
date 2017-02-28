#Tristan Wickliff
#Foundations of Programming 100B
#HW7


"""Finish the user option to delete an entry from the dictionary by removing the "pass" statements 
        and adding code to delete a user by name 
        (extra challenge: can you figure out how to delete a user by name OR username?)
Finish the user option to lookup a username by name by removing the "pass" statement 
        and adding code to find a user by name 
Run the script and make sure each option works
Add exception handling to each user input option.
Add doc strings to the script and comment the code.
Push your finished script to your personal, publicly accessible Github repo.  
Submit a link to the Github repo containing your script on canvas.""" 

from collections import OrderedDict
from sortedcontainers import SortedDict

def print_menu(): 
    """The print_menu function stores users and their associated user name. 
The function allows you to add and remove users, as well as look up users by name."""
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a User')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'
usernames['Tristan']= '|Sneak|'

# setup counter to store menu choice
menu_choice = 0

print_menu()

# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("Menu choice must be entered as an integer.\n")

    
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        if name not in usernames:
            username = input("User Name: ")
            while username in usernames.values():
                print("Username already taken. Please enter a new username: ")
                username = input("User Name: ")
            usernames[name] = username

        else:
            print(name + " already has a username.")

        
    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        print("1. By name.")
        print("2. By username.")
        try:
            bywhat = int(input("Type in a number (1-2): "))
        except ValueError:
            bywhat = int(input("Menu choice must be entered as an integer. Type in a number (1-2): "))
        if bywhat==1:
            name = input("Name: ")
            if name in usernames:
                del usernames[name]
            else:
                print("Name not found.")
        elif bywhat ==2:
            usname = input("Username: ")
            if usname in usernames.values():
                for name, user in usernames.iteritems():
                    if user == usname:
                        del usernames[name]
            else:
                print("Username not found.")
        else:
            print("Invalid choice. Returning to main menu.")

            

    # view user name      
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("Username is " + str(usernames[name]))
        else:
            print("User not found.")
    
    # is user enters something strange, show them the menu
    elif menu_choice != 5:
       print_menu()
