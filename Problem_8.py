#                   Author : Richard Feeney Started: 26/02/2019

#                                    Problem 8 :    
#      Write a program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 


import datetime #Import the datetime module

current = datetime.datetime.now() # Use datetime.no() to get the current date and time
print("\n")

print("The current date and time is :",(current.strftime("%A, %B, %Y at %I:%M %p"))) # strftime is used format / pull different information from date by using the %? 

