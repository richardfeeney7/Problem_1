#                   Author : Richard Feeney Started: 14/03/2019

#                                    Problem 10 : 
#    
#      Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].
 

import matplotlib.pyplot as mp # Import matplotlib and give it an alias of p
import numpy as ran # Import numpy and define alias of ran

# x = 1,2,3,4  TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'. Will import numpy

# numpy.arange([start, ]stop, [step, ]dtype=None) How .arange is structured. Since we start at 0 I wont input 0 as this is the default starting point
x = ran.arange(4) # Return evenly spaced values within the given range. form 0 to 4 not including 4. Change 4 to 5 if we wish to include 4

mp.title("Question 10 Graph") # Add graph Title
mp.xlabel("X Axis")           # Add title on x axis
mp.ylabel("Y Axis")           # Add title on y axis
mp.grid(True)                 # Add grid onto graph for easier viewing

#mp.legend(["y = x","y = x^2", "y = 2x"]) Moved below the plottong 

a = x       # function x as given in the question
y = x*x     # function x^2 as given in the question
z = 2**x    # function 2x as given in the question

mp.plot(x, a) # Plot f(x)
mp.plot(x, y) # Plot f(x**2)
mp.plot(x, z) # Plot f(2**x)

mp.legend(["y = x","y = x^2", "y = 2x"], loc="upper center") # Added ro lock it in the center of the graph

mp.show() # Display the graph

