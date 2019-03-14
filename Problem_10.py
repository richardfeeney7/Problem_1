#                   Author : Richard Feeney Started: 14/03/2019

#                                    Problem 10 : 
#    
#      Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].
 

import matplotlib.pyplot as p # Import matplotlib and give it an alias of p

x = (0, 1, 2, 3, 4) # Set X values in an array 

a = x
y = x**2
z = 2**x



p.plot(x, a)
p.plot(x, y)
p.plot(x, z)

# to display the graph

p.show()

