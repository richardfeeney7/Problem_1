#                   Author : Richard Feeney Started: 17/02/2019

#                                    Problem 1 :                                                                         Write a program that asks the user to input any positive integer and outputs the                                               sum of all numbers between one and that number.  



#Below print("\") statement will give space between sentences for the user to read and or input
print("\n")

# User input is stored in num. And I and Y are set to 0 and Y will be used to store user input when they are asked if they want to try again if its a negative number and I will be used to store num -1. #
num = int(input ("Please enter a positive number : "))
#i , y = 0, 0 This is another way to say i = y = 0
i = y = 0

#This while loop will check num to see if it it less than 0. If true it will ask the user to try again. If the user enters Y it will loop and do it again ELSE it will exit the application. 
while num < 0:
    print("\n")
    #The try_again1 variable is used to store the input from the user asking if they want to try again.

    try_again1 = input("Negative number. Would you like to try another number  'Y' or 'N' ? : ")
    #The if statment checks if the user enters Y or y and if anything else is entered it will exit the application.

    if try_again1 == "Y" or try_again1 == "y":
        print("\n")
        num = int(input("Please try again by entering a positive number : " ))
    else:
        print("\n")
        print("Thank you for using this application. I hope that you will use it again see you soon ")
        break

#ELSE within the while loop that checks if num is < 0 and if num > 0 it will use the while loop in this section.
else: 

    #WHILE checks is num is > 0 and if so it will add NUM to i and that number will be stored in i and num will be decreased by one and loop until num > 0 and each time i will be updated by added it to the current num.
    while num > 0:
        i = i + num
        num = num - 1 
    
    #This ELSE is whitin the WHILE num > 0 to output the final number for i and ask if they want to try again.
    else:
        print("\n")
        print("The sum of all the numbers between one and your number is " , i )
        print("\n")
        #try_again will store the responce if the user wants to try again or not. 
        try_again = input("Thank you for using the application.Would you like to try another number  'Y' or 'N' ?  ")

        #if the user wants to try again the while loop haas a nested while loop to do the same calculation as the about while num > 0 on line 33 but instead of using i again I have used y. 
        while try_again == "Y" or try_again == "y":
            print("\n")
            num = int(input("Please try entering a positive number again : " ))
            while num > 0:
                y = y + num
                num = num - 1 

                
            #if the user input was not to try again it will out the number in y
            else:
                print("\n")
                print("The sum of all the numbers between one and your number is " , y )
                break
        # Thank the user for using the application 
        else:
            print("\n")
            print("Thank you for using this application. I hope that you will use it again see you soon ")
    