""" Author : Richard Feeney 
    Started: 17/02/2019
"""

"""                                   Problem 1 :
        Write a program that asks the user to input any positive integer and outputs the
        sum of all numbers between one and that number.  
"""

print("\n")
num = int(input ("Please enter a positive number to compute : "))
i = 0

while num < 0:
    print("\n")
    #print( "The number must be a positive number ")
    num = int(input("That was a negivive number, please try again by entering a positive number : "))

while num > 0:
    i = i + num
    num = num - 1 

print("\n")
print("The sum of all the numbers between one and your number is " , i )