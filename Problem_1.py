""" Author : Richard Feeney 
    Started: 17/02/2019
"""

"""                                   Problem 1 :
        Write a program that asks the user to input any positive integer and outputs the
        sum of all numbers between one and that number.  
"""

print("\n")
num = int(input ("Please enter a positive number : "))
i = 0
y = 0

while num < 0:
    print("\n")
    try_again1 = input("Negative number. Would you like to try another number  'Y' or 'N' ? : ")
    if try_again1 == "Y" or try_again1 == "y":
        print("\n")
        num = int(input("Please try again by entering a positive number : " ))
    else:
        print("\n")
        print("Thank you for using this application. I hope that you will use it again see you soon ")
else: 
    while num > 0:
        i = i + num
        num = num - 1 

    else:
        print("\n")
        print("The sum of all the numbers between one and your number is " , i )
        print("\n")
        try_again = input("Thank you for using the application.Would you like to try another number  'Y' or 'N' ?  ")
        print("\n")
        while try_again == "Y" or try_again == "y":
            print("\n")
            num = int(input("Please try entering a positive number again : " ))
            while num > 0:
                y = y + num
                num = num - 1 
            else:
                print("\n")
                print("The sum of all the numbers between one and your number is " , y )
                break
        else:
            print("Thank you for using this application. I hope that you will use it again see you soon ")
    