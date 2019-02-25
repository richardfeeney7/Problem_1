#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 5 :    
# Write a program that asks the user to input a positive integer and tells the user whether or not the number 
#                                     is a prime.       


num = int(input("Please enter a positive number : ")) # Accepts the user number to be checked if it is prime
#y=2 Not needed as I used a range function instead. 

''' if num % y == 0:
    print("Your number ",num, " is NOT a prime") 
else:
    print("Your number ",num, " is a prime")
'''
# If statement above didn't give me the desired output. I have used the range function instead.

for i in range(2, num): #Create the range function and set i = 2
    if num % i == 0:    #If the user input Mod i == 0 do this print not prime 
        print("Sorry but ",num, " is not prime")
        break
else:
    print("Yes ",num, "is a prime number")     
