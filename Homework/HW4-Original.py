#Tristan Wickliff
#IT Foundations 100 B
#Assignment 4
#HW4.py


#Download the file "airports.dat" from this webpage: http://openflights.org/data.html (Links to an external site.)
#Write a python script called HW4.py
#Import the csv module
#Write a function that only prints out information for airports in Russia or Australia
#Optional: Write a function that counts the number of airports in each country and prints out the total counts.

import csv
import sys

"""I was having issues by simply using "save file as" when trying to download the .dat file
In order to fix this I opened the file in the browser, copied all of its contents,
and then saved my own airports.dat file. In addition, the airports file has one airport 
listed as in the US, but it is actually in Australia - see item 9533 - Cowra"""

def russ_aus (file):
	f = open(file, "r")
	for row in csv.reader(f):
		if "Russia" in row[0]:
			print("\n" + row[0])
		if "Australia" in row[0]:
			print("\n" + row[0])
	f.close()
	return 
	
russ_aus("./airports.dat")	

input("\nHit Enter to Continue")

"""The below function was my attempt at printing out the number of aiports in each country.
I was unsuccesful however. It works for the first country, but then i cant get the count to 
start over again."""
def airports_per_country (file):
	f = open(file, "r")
	readv = csv.reader(f)
	countrylist = []
	addcountry=[""]
	for row in readv:
		data = row[0]
		new_data=data.split(",")
		country = new_data[3].strip("\"")
		if country not in countrylist:
			addcountry[0]=country
			countrylist+=addcountry
			cll=len(countrylist)
	f.close()		
	
	countrycount=[0]*cll	
	location=0
	f2 = open(file, "r")
	readv2 = csv.reader(f2)
	count=0
	#for each country in my country list
	for cil in countrylist:
		scil=cil.strip(" ")
	#iterate through each row of file
		for row2 in readv2:
	#row in file contains the country, add to country counter
			if scil in row2[0]:
				count+=1
		print(scil + " has " + str(count) + " airports.")
		countrycount[location]=count
		location+=1
		count=0
	f2.close()		
	return countrylist,countrycount

#airports_per_country("./airports.dat")

#input("\nHit Enter to Exit")
