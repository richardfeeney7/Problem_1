#                              Author : Richard Feeney
#                               Started: 17/02/2019

#                                    Problem 1 :   
#                                                                       
#  Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.  


'''User input is stored in num. And i and y are set to 0, y will be used to store user input when they are asked if they want to try again '''

def pos_num(num) :  # Define the function that will accept user input and store it in num
    i = y = 0       # Set i and y to 0
    while num < 0:  # Loop will check num to see if it it less than 0.
        print("\n")

        #The try_again1 variable is used to store the input from the user when asked if they want to try again.
        try_again1 = input("Negative number. Would you like to try another number  'Y' or 'N' ? : ")

        #The if statement checks if the user enters Y or y, if anything else is entered it will exit the application.
        if try_again1 == "Y" or try_again1 == "y":
            print("\n")
            num = int(input("Please try again by entering a positive number : " ))
        else:
            print("\n")
            print("Thank you for using this application. I hope that you will use it again see you soon ")
            break

    else: 

        # WHILE checks is num > 0,if True it will add num to i and this will be stored in i then num will be decreased by one and loop until num > 0 and each time i will be updated by added it to the current num.
        while num > 0:
            i = i + num
            num = num - 1 
            #print("The sum of all the numbers between one and your number is " , i ) # Moved to line 33 as multiple lines were outputting

        else:
            print("\n")
            print("The sum of all the numbers between one and your number is " , i )
            print("\n")

            #try_again will store the responce when the user is asked if they want to try again. 
            try_again = input("Thank you for using the application.Would you like to try another number  'Y' or 'N' ?  ")

            #if the user wants to try again the while loop has a nested while loop to do a similar calculation to the the loop at line 26
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

            # Thank the user for using the application 
            else:
                print("\n")
                print("Thank you for using this application. I hope that you will use it again see you soon ")

pos_num(int(input ("Please enter a positive number : "))) # Send number to the function
    