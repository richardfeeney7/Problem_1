# Author Richard Feeney
# Date 21/02/2017

#                                        Problem 3 : 
 
#     Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12. 

for x in range(1000,1501):
    if (x%6 == 0 and x%12 == 0):
          print(x,"Sorry divisable by 6 and 12")

    elif (x%6 == 0):
        print(x, "Divisable by 6")