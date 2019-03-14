#                   Author : Richard Feeney Started: 14/03/2019

#                                    Problem 10 : 
#    
#      Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].
 

import matplotlib.pyplot as p # Import matplotlib and give it an alias of p
import numpy as ran # Import numpy and define alias of ran

# x = 1,2,3,4  TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'. Will import numpy

# numpy.arange([start, ]stop, [step, ]dtype=None) How .arange is structured
x = ran.arange(0, 4) # Return evenly spaced values within the given range. form 0 to 4 not including 4. Change 4 to 5 if we wish to include 4

a = x    
y = x**2
z = 2**x



p.plot(x, a)
p.plot(x, y)
p.plot(x, z)

# to display the graph

p.show()

