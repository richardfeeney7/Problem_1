# Author Richard Feeney
# Date 22/02/2017

#                                        Problem 4 : 
 
'''    Write a program that asks the user to input any positive integer and outputs the successive values 
       of the following calculation. At each step calculate the next value by taking the current value and,
       if it is even,divide it by two,but if it is odd,multiply it by three and add one.
'''

num = int(input("Please enter a positive number : ")) #Store user input in num

while num > 1:
    if num % 2 == 0:
       num = num/2
       print(num)

    else:
        num = (num*3) + 1
        print(num) 

