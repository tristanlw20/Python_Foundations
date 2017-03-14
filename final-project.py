"""
Tristan Wickliff
IT Foundations 100B
Final Project
"""


import sys
import csv
import pandas as pd
from collections import OrderedDict
from sortedcontainers import SortedDict

def print_menu (sys.argv[1], sys.argv[2])
	"""This script is used to stores user's favorite NHL teams. The user
	passes in their name and favorite team, which then get stored in a dictionary
	that can be used for analysis of the entries."""
	print ("1. Print Users")
	print ("2. Add Users")
	print ("3. View Team Counts")
	print ("4. Graph Team Counts")
	print ("5. Quit")

# Create dictionary with key = Names, value = user_name
nhlpicks = SortedDict()
nhlpicks['Tristan'] = 'San Jose Sharks'
nhlpicks['Daniel'] = 'Colorado Avalanche'
nhlpicks['Robby'] = 'San Jose Sharks'
nhlpicks['Robb'] = 'Colorado Avalanche'
nhlpicks['CJ'] = 'Pittsburgh Penguins'
nhlpicks['Tristan']= '|Sneak|'

nhlteams = ["Carolina Hurricanes", "Columbus Blue Jackets","Colorado Avalanche","San Jose Sharks", 
	"New Jersey Devils", "New York Islanders", "New York Rangers", "Philadelphia Flyers", 
	"Pittsburgh Penguins", "Washington Capitals", "Boston Bruins", "Buffalo Sabres", "Detroit Red Wings",
	"Florida Panthers", "Montreal Canadiens", "Ottawa Senators", "Tampa Bay Lightning", 
	"Toronto Maple Leafs", "Chicago Blackhawks", "Dallas Stars", "Minnesota Wild", "Nashville Predators", 
	"St. Louis Blues", "Winnipeg Jets", "Anaheim Ducks", "Arizona Coyotes", "Calgary Flames", 
	"Edmonton Oilers", "Los Angeles Kings", "Vancouver Canucks"]

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
        assert (menu_choice==1), "Not sure how i got here..."
        print("Current Users:")
        for x,y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        assert (menu_choice==2), "Not sure how i got here..."
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
        #remove an entry by name
        if bywhat==1:
            name = input("Name: ")
            if name in usernames:
                del usernames[name]
            else:
                print("Name not found.")
        #remove an entry by username
        elif bywhat ==2:
            usname = input("Username: ")
            if usname in usernames.values():
                for name, user in usernames.iteritems():
                    if user == usname:
                        del usernames[name]
            else:
                print("Username not found.")
        #print message if 1 or 2 was not chosen
        else:
            print("Invalid choice. Returning to main menu.")

            

    # view user name      
    elif menu_choice == 4:
        assert (menu_choice==4), "Not sure how i got here..."
        print("Lookup User")
        name = input("Name: ")
        if name in usernames:
            print("Username is " + str(usernames[name]))
        else:
            print("User not found.")
    
    # if user enters something strange, show them the menu
    elif menu_choice != 5:
       assert (menu_choice!=5), "Not sure how i got here..."
       print_menu()
