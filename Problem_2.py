# Author Richard Feeney

#                                     Problem 2 : 
 
#         Write a program that outputs whether or not today is a day that begins with the letter T. 

   


import datetime #Import the datetime module. 
tdate = datetime.date.today() #This will find todays dats and store it in tdate where i will uses later.

print("\n") 
# Below print is a welcome message for the user.
print("Hello and welcome to the application that will tell you if the day begins with a letter T" )
print("\n")   

if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3: # 0 = Monday, 1 = Tuesday etc up to 6 that is = Sunday
  print("Great news :) todays date is :",tdate , "and begins with the letter T")
else:
  print("Unfortunately today does not start with a T :) .")





from datetime import datetime
print (datetime.now().weekday()==3)