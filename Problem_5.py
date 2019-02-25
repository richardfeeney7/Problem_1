#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 5 :    
# Write a program that asks the user to input a positive integer and tells the user whether or not the number 
#                                     is a prime.       


x = int(input("Please enter a positive number : "))
y = 2


if x > 0:
    if x % y == 0:
        print("Your number ",x, "is prime") 
    else:
        print("Not prime")
