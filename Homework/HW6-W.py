#Tristan Wickliff
#IT Foundations 100 B
#Assignment 6
#HW6.py


#Download the iris dataset  (Links to an external site.)
#Download the iris script we went over in class (Links to an external site.)
#Change the read_in_csv() function to require the user to specify the input file path at runtime 
	#(hint: use sys.argv)
#Finish creating a function to calculate the average overall sepal length 
#Create a function to calculate average petal length based on class name 
	#(hint: create a function that accepts class name as a parameter) 
#Add a try/except statement to each function
#Print the output to standard out (your terminal)
#Turn in your python script


import sys
import csv

def read_in_csv():
	try:
		f = open(sys.argv[1])
		my_file = csv.reader(f)
	except FileNotFoundError:
		f = open(input("You provided an invalid file name. What is the correct file name?"))
		my_file = csv.reader(f)
	return my_file

def get_column_unique(col_number):
	col_list = []
	my_file = read_in_csv()
	for row in my_file:
		col_list.append(row[col_number])
	unique_vals = set(col_list)
	unique_length = len(unique_vals)
	return unique_length    

def count_things(col_number):
    my_dict = {}
    my_file = read_in_csv()
    
    # loop through dictionary to track name and count
    for row in my_file:
        key_name = row[col_number]
        
        # for every row, check if the class_name is in the dictionary
        if key_name in my_dict:
            my_dict[key_name] = my_dict[key_name] + 1
        
        # if not, add it, and set the count to 1
        else:
            my_dict[key_name] = 1
    
    return my_dict

#function to calculate the average overall sepal length
def avg_sepal_overall():
	#column 0 in file is sepal length
	my_file = read_in_csv()
	sep_len = 0
	entry=0
	for row in my_file:
		sep_len+=float(row[0])
		entry+=1
	aso = sep_len/entry
	return aso

#function to calculate average petal length based on class name (hint: create a function that accepts class name as a parameter)
def avg_petal_class():
	plength = 0
	classentries = 0
	my_file = read_in_csv()
	classname = sys.argv[2]
	for row in my_file:
		if classname.lower()==row[4].lower():
			classentries+=1
			plength += float(row[2])
	try:
		avg_p_length = plength/classentries
	except ZeroDivisionError:
		print("That class does not exist.")
		avg_p_length = 0
	return [avg_p_length, classname]


unique_vals = get_column_unique(4)
count_classes = count_things(4)
avg_sep_overall = avg_sepal_overall()
avg_petal_length = avg_petal_class()
#print(unique_vals)
#print(count_classes)
print("The average overall sepal length for all iris classes is {}cm.".format(avg_sep_overall))
if avg_petal_length[0] !=0:
	print("The average {} petal length is {} cm.".format(avg_petal_length[1],avg_petal_length[0]))
