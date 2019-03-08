# Author Richard Feeney
# Date 21/02/2017

#                                        Problem 2 : 
 
#         Write a program that outputs whether or not today is a day that begins with the letter T. 


import datetime as dt #Import the datetime module and give it an alias

d = dt.datetime.now() #This will input the current date into d where i will use in my else print statement
#print(d) # Testing to see the date format and how it looks

tdate = dt.datetime.today().weekday() #This will find todays date and store it in tdate where i will uses later.
#print(tdate) # Testing to see the output from dt.datetime.today().weekday(). It will output a number

print("Hello and welcome to the application that will tell you if the day begins with a letter T" )
print("\n")   


''' if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
    
    I created a variable called tdate to use in the active if statement as the commented out if on line 21 statement was very long.
    This will use the date starting from position 0 = Monday, 1 = Tuesday etc up to 6 that is = Sunday,
    isoweekday could be used that would start from 1 = Monday to 7 = Sunday
'''

if tdate == 1 or tdate ==3: # Instead of using the longer if above i created a var tdate to store current date.

    print(" Today starts with a T")# I orginally used tdate in this print but change to use the strftime method instead
    print("Great news :) todays is" ,d.strftime("%A"), "and begins with the letter T") #This will tell the user what day it is and that it does not start with a T
    # Steftime("%A") will display the full weekday name and if its Tue or Thurs is will output 
    
else:
    print("Unfortunately today is",d.strftime("%A"), "does not start with a T :) .") 

