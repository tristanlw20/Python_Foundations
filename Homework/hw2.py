#Tristan Wickliff
#IT Foundations 100 B
#Assignment 2
#hw2.py

#Ask a user to input a string, integer and a float and assign them to separate variables

#String input
string = input("Please input a string here by answering the question \"What is your middle name?\": ")

#Integer input
integer = int(input("\nPlease input an integer such as 1, 9, 30, etc: "))

#Float input
floaty = float(input("\nPlease input a float here such as 1.25, 2.999, 21.212121, etc: "))

#Use string formatting to print out the statement "You input {user_string} as your string." 
#Print out similar statements for an integer and a float. 

#String formatting with string input
print("\nYou input {} as your string.".format(string))

#String formatting with integer input
print("\nYou input {} as your integer.".format(integer))

#String formatting with float input
print("\nYou input {} as your float.".format(floaty))

#Double your input (write it twice, or multiply by 2, depending on data type)
#and print out the results, using string formatting to describe what you did
#to the user input. 

#Doubling the string
print("\nThis is your string, twice! {}".format(string*2))
#print("\nThis is your string, twice! {} {}".format(string, string))
#Doubling the integer
print("\nThis is your integer, doubled! {}".format(integer*2))

#Doubling the float
print("\nThis is your float, doubled! {}".format(floaty*2))

#Concatenate the input string and the input float using string formatting to make a sentence
#Print it out.
print("\nMy middle name is {} and the float I entered was {}".format(string, floaty))

#Use string formatting to print out the "This is your integer, centered: " with a new line
#followed by the user's input integer centered. 
print("\nThis is your integer, centered:\n{:^31}".format(integer))

input("\nPress \"Enter\" to exit the program.")




