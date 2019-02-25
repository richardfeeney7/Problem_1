#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 5 :    
# Write a program that asks the user to input a positive integer and tells the user whether or not the number 
#                                     is a prime.       


print("\n")
name = input("Hello and welcome to my application, please input your name ? ")
print("\n")
num = int(input("Please enter a positive number : ")) # Accepts the user number to be checked if it is prime

'''
y=2
if num > 1:
    if num % y == 0:
        print("Your number ",num, " is NOT a prime") 
    else:
        print("Your number ",num, " is a prime")
'''
# If statement above didn't give me the desired output. I have used the range function instead.
print("\n")

if num > 1:
    for i in range(2,num): #Create the range function and set i = 1
        if num % i == 0:    #If the user input Mod i == 0 do this print not prime 
            print("Sorry", name ,num, "is not prime")
            break
    else:
        print("Yes", name, num, "is a prime number")   
elif num == 1: # 1 cant be a prime number aas it only has 1 factor
    print("Sorry", num, "is not a prime number")  
elif num < 0:
    print("A prime number cant be a negative number")
