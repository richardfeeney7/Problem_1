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
    try_again = input("Negative number. Would you like to try another number  'Y' or 'N' ?  ")
    if try_again == "Y" or try_again == "y":
        print("\n")
        num = int(input("Please try again : " ))
    else:
        print("\n")
        print("Thank you for using this application today, see you soon ")
        break
else: 
    while num > 0:
        i = i + num
        num = num - 1 
    else:
        print("\n")
        print("The sum of all the numbers between one and your number is " , i )
        print("\n")
        print("Thank you for using this application today, see you soon ")
