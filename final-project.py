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
import matplotlib.pyplot as plt

def write_input(word1, word2):
    """This is purely to meet the project criteria. The user will use system arguments,
    any of their choosing, and simply be written to the writeto.txt file."""
    f=open("writeto.txt", "w+")
    f.write("The first system arguement was {} and the second was {}.".format(word1, word2))
    f.close()
write_input(sys.argv[1], sys.argv[2])

def print_menu ():
	"""This script is used to stores user's favorite NHL teams. The user
	passes in their name and favorite team, which then get stored in a dictionary
	that can be used for analysis of the entries."""
	print ("1. Print Fans")
	print ("2. Add Fan")
	print ("3. View Team Fan Counts")
	print ("4. Graph Team Fan Counts")
	print ("5. Quit")

# Create dictionary with key = Names, value = user_name
nhlpicks = SortedDict()
nhlpicks['Tristan'] = 'San Jose Sharks'
nhlpicks['Daniel'] = 'Colorado Avalanche'
nhlpicks['Robby'] = 'San Jose Sharks'
nhlpicks['Robb'] = 'Colorado Avalanche'
nhlpicks['CJ'] = 'Pittsburgh Penguins'
nhlpicks['Katie']= 'Chicago Blackhawks'

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
        print("Current Fans:")
        for x,y in nhlpicks.items():
            print("Name: {} \tFavorite Team: {} \n".format(x,y))
            
    # add an entry
    elif menu_choice == 2:
        assert (menu_choice==2), "Not sure how i got here..."
        print("Favorite NHL Team")
        name = input("Name: ")
        if name not in nhlpicks:
            nhlpick = input("Favorite Team: ")
            while nhlpick not in nhlteams:
            	nhlpick = input("NHL team does not exist. Choose another team. Favorite Team:")
            nhlpicks[name] = nhlpick
        else:
            print("{} already pledged allegience to the {}!".format(name, nhlpicks[name]))

        
    # view team fan counts
    elif menu_choice == 3:
        assert (menu_choice==3), "Not sure how i got here..."
        fanteam = input("NHL Team: ")
        teamcount = 0
        if fanteam in nhlteams:
            teamcount = 0
            for team in nhlpicks.values():
                if fanteam == team:
                    teamcount+=1
            print("Of the {} teams in the NHL, the {} have {} dedicated fans.".format(len(nhlteams),fanteam, teamcount))
        else:
            print("That is not an NHL team.")

        
    # graph team fan counts     
    elif menu_choice == 4:
        assert (menu_choice==4), "Not sure how i got here..."
        fantotals=SortedDict()
        for team in nhlpicks.values():
            teamcount=0
            if team not in fantotals.items():
                for tc in nhlpicks.values():
                    if tc==team:
                        teamcount+=1
            fantotals[team]=teamcount

        tosave = plt.figure("Dedicated Fans for an NHL Team")
        plt.bar(range(len(fantotals)), fantotals.values(), align='center')
        plt.xticks(range(len(fantotals)), fantotals.keys())
        plt.xticks(rotation=6)
        plt.ylabel("Dedicated Fan Count")
        plt.xlabel("NHL Teams")

        #plt.show()
        tosave.savefig("fancount.pdf")
        print("Graph printed to fancount.pdf")
        
    # if user enters something strange, show them the menu
    elif menu_choice != 5:
       assert (menu_choice!=5), "Not sure how i got here..."
       print_menu()


