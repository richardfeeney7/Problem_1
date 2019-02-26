#                   Author : Richard Feeney Started: 26/02/2019

#                                    Problem 8 :    
#      Write a program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”. 


import datetime
# Use the satetime object to use in strings

current = datetime.datetime.now()
print("\n")

print("The current date and time is : ",(current.strftime("%A, %B, %Y at %I:%M %p")))
# strftime is used format / pull different information from date by using the %? 

