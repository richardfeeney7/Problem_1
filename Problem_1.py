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
count=1

while num < 0:
    print("\n")
    #print( "The number must be a positive number ")
    num = int(input("That was a negivive number, please try again by entering a positive number : "))
    if num < 0:
        print("\n")
        try_again = input("Another negative number. Would you like to try another number  'Y' or 'N' ?  ")
        if try_again == "Y" or try_again == "y":
            print("\n")
            num = int(input("Please try again : " ))
        else:
            break

while num > 0:
    i = i + num
    num = num - 1 

print("\n")
print("The sum of all the numbers between one and your number is " , i )

print("\n")
try_again = input("Would you like to try another number  'Y' or 'N' ?  ")
if try_again == "Y" or try_again == "y":
    print("\n")
    num = int(input("Please try again : " ))