#Tristan Wickliff
#IT Foundations 100 B
#Assignment 5
#HW5.py


#Using the airports.dat file from HW4 (copy and paste from the web to a text file)
#Read the file in using CSV reader as you did in HW4
#Use a dictionary to count the number of airports in the file by tracking the country name and count per country.
#Use your country count data from step 2 to:
	#Find the country with the most (max) entries (rows)
	#Find the country with the least (min) entries (rows)
	#Find the average (mean) number of entries per country
#Use string formatting to print out this information in a pretty way
#Save the output to a file named HW5.txt (see the lecture notes from module 4)
#Turn in HW5.py and HW.txt

import sys
import csv

f=open("./HW.txt", 'r', encoding='UTF8')
nf=csv.reader(f, delimiter = ",")

#cc will be the country count dictionary
cc={}

#turning file in to a list
for row in nf:
	data = row[3]
	country = data.strip("\"")
	if country not in cc:
		cc[country] = 1
	else:
		cc[country]+=1

print(cc.items())