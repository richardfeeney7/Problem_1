# Author Richard Feeney

#                                     Problem 2 : 
 
#         Write a program that outputs whether or not today is a day that begins with the letter T. 


import datetime #Import the datetime module. 
d = datetime.datetime.now() #This will input the current date into d where i will use in my else print statement
tdate = datetime.datetime.today().weekday() #This will find todays date and store it in tdate where i will uses later.

print("\n") 
# Below print is a welcome message for the user.
print("Hello and welcome to the application that will tell you if the day begins with a letter T" )
print("\n")   

#isoweekday could be used that would start from 1 = Monday to 7 = Sunday
#if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: # 0 = Monday, 1 = Tuesday etc up to 6 that is = Sunday


#instead of using the longer if above i created a var tdate to store current date.
if tdate == 1 or tdate ==3: 
    #I orginally used tdate in this print but change to use the strftime method instead
    #steftime("%A") will display the full weekday name and if its Tue or Thurs is will output 
    print("Great news :) todays is",#tdate  ,
    d.strftime("%A"), "and begins with the letter T")
    
    #This will tell the user what day it is and that it does not start with a T
else:
    print("Unfortunately today is",d.strftime("%A"), "does not start with a T :) .") 

