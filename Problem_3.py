# Author Richard Feeney
# Date 21/02/2017

#                                        Problem 3 : 
 
#     Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 

for x in range(1000,10000):
    if (x%6 == 0):
        print(x)
    if(x%6 ==0 and x%12 ==0):
        print("Sorry but divisable by both 6 and 12")