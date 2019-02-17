""" Author : Richard Feeney 
    Started: 17/02/2019
"""

"""                                   Problem 1 :
        Write a program that asks the user to input any positive integer and outputs the
        sum of all numbers between one and that number.  
"""

num = int(input ("Please enter a positive number to compute : "))
i = 0

if num < 0:
    (print( "The number must be a positive number "))
    num = int(input("Please try again by entering a positive number : "))

while num > 0:
    i = i + num
    num = num - 1 

print(i)