#                                     Author Richard Feeney
#                                       Date 21/02/2017

#                                        Problem 2 : 
 
#         Write a program that outputs whether or not today is a day that begins with the letter T. 


import datetime as dt #Import the datetime module and give it an alias

d = dt.datetime.now() #This will input the current date ans store it in d.
#print(d) # Testing to see the date format and how it looks

tdate = dt.datetime.today().weekday() #This will find todays date and store it in tdate where i will uses later.
#print(tdate) # Testing to see the output from dt.datetime.today().weekday(). It will output a number to represent the day of the week.

print("Hello and welcome to the application that will tell you if the day begins with a letter T" )
print("\n")   

''' if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
    
    I created a variable called tdate to use in the active if statement below because the if statement commented out on line 20 statement was long and could be shortened
    and this will generate the day starting from position 0 = Monday, 1 = Tuesday etc up to 6 that is = Sunday,
    
    isoweekday could be used that would start from 0 = Monday to 6 = Sunday
'''

if tdate == 1 or tdate ==3: # Finds the days by their position from 0 Monday to 6 Sunday

    print(" Today starts with a T") # I orginally used tdate in this print but change to use the strftime method instead
    print("Great news :) todays is" ,d.strftime("%A"), "and begins with the letter T") # This will tell the user what day it is and that it starts with a T
    # Steftime("%A") will display the full weekday name and if its Tue or Thurs
    
else:
    print("Unfortunately today is",d.strftime("%A"), "does not start with a T :) .") 
