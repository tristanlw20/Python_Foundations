#Tristan Wickliff
#IT Foundations 100 B
#Assignment 3
#hw3.py

#Write a function that takes a minimum and maximum number as an arguement
def min_max(var1, var2):
	"""This function is able to take both integers or floats, but the floats ALWAYS round down.
	The program loses the original value of floats and only returns integers.
	This function could likely be constructed better to not use the same for loop twice.
	I specifically chose to not include 0 as a number divisible by 3, however without
	the compound condition it would have been included."""
#Convert the numbers to integers and store in a list	
	numrange = [int(var1), int(var2)] 
#Sort the list	
	numrange.sort()
#Specify the minimum and maximum values in the list	
	min = numrange[0]
	max = numrange[1]
#Place all values between min and max in a new list	
	range_list = list(range(min + 1, max))
#Print each value in the new list	
	for i in range_list:
		print(i)
#Print each value along with the index in the list at which it is located		
	for index, number in enumerate(range_list):
		print("This number, " + str(number) + ", is at index " + str(index) + " in the list.") 
#Print out the numbers in the list divisible by 3		
	for i in range_list:
		if i%3==0 and i!=0:
			print("The number {} is divisible by 3.".format(i))
				
	return range_list

#Invoke min_max function using floats	
min_max(5.922,-9.333)

#Invoke min_max function using ints
#min_max(0,-20)
input("\nPress 'Enter' to exit the program.")

