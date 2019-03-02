#                   Author : Richard Feeney Started: 26/02/2019

#                                    Problem 7 :    
#          Write a program that takes a positive ﬂoating point number as input and outputs an 
#                           approximation of its square root. 

import math # Import and use the math module

def sqrt(num):      # Define function
    if(num > 0):    # Start if statement
        num2 = (math.sqrt(num)) # Take user input num and use the math.sqrt to find the square root and store it in num2

        print("The square root of ", num, "is  = " ,round(num2,2)) # Output the square root that is stored in num2 and round it to two decimal places
    else:
        print("Please input a positive number ! ")

sqrt(int(input("Please enter in a number containing decimals : "))) # Use int to accept a decimal input from the user and store in num. 
