# Author Richard Feeney
# Date 21/02/2017

#                                         Problem 3 : 
 
#     Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 


''' I had this block of code written before I read the question properly. The output will show what is divisible by 6 alone and what is 
    divisible by both 6 and 12 together. 

 I used the range function to return the sequence of numbers starting from 1000 and increments by 1

 for x in range(1000,10001): #Set to 10001 so 10000 is included
    if (x%6 == 0 and x%12 == 0):
          print(x,"Sorry divisible by 6 and 12")

   elif (x%6 == 0):
       print(x, "Divisible by 6")
'''

#for x in range(1000,10000):       x is the var that will increment by 1 starting from 1000 until it reaches 10000 and stops.
for x in range(1000,10001):        # Set to 10001 so 10000 is included as the for loop above did not include 10000
   
    if (x%6 == 0 and x%12 == 0):   # % looks for a remainder and if it = 0 it is true. X is used to store the number up to 10000 as it loops the for loop
       pass                        # I want the if statement to execute but not to print anything so I have included pass. 

    elif (x%6 == 0):               # Below is the output if mod of 6 = 0. It will print the number.
       print(x, "Divisible by 6")
