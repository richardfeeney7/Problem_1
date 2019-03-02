# Author Richard Feeney
# Date 21/02/2017

#                                        Problem 3 : 
 
#     Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 


''' I had the below code written before I read the question properly. I have rewritten the code below it

 # I used the range function to return the sequence of numbers starting from 1000 and increments by 1

 for x in range(1000,10001): #Set to 10001 so 10000 is included
    if (x%6 == 0 and x%12 == 0):
          print(x,"Sorry divisible by 6 and 12")

   elif (x%6 == 0):
       print(x, "Divisible by 6")
'''

                            # x is the var that will increment by 1 starting from 1000 until it reaches 10000 and stops.
for x in range(1000,10001): # Set to 10001 so 10000 is included
   
    if (x%6 == 0 and x%12 == 0):   # % looks for a remainder and if it = 0 it is true.
         pass                      # I want the if statement to execute but not to print anything

    elif (x%6 == 0):        # Below is the output if mod of 6 = 0. It will print the number.
       print(x, "Divisible by 6")
