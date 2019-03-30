#                              Author : Richard Feeney 
#                               Started: 10/03/2019

#                                    Problem 9 :    
#      Write a program that reads in a text ﬁle and outputs every second line. ”. 




import sys # Import the sys library

# print(sys.argv) # Print the list of Arguments.

try: # Test the below block of code for errors
    len(sys.argv) > 1  # If greater than one then the user has entered in arguments. (I could have wrote == 2 instead of > 1)
    with open(sys.argv[1], 'r') as f:    # sys.argv[1] is the first commant line argument passed (ie Q9_File.py)
        line = f.readlines()             # reads the lines in teh file and store in line.
        for i in range(0, len(line), 2): # Loop the document and print every second line starting from position 0
            print(line[i])               # Print every second line to the screen
             
except: # Handle the error - Output the print statement
    print ("Please specify an argument ie: python Problem_9.py Q9_File.txt.")
    sys.exit()

# Below f.writes have already written these lines to my text file so I have commented them out. 
'''
with open("Q9_File.txt", "w") as f: #recommended way to use as it will close once the indent finishes.
        f.write("Title  :  What is Python \n")
        f.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. \n")
        f.write("Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as ascripting or glue language to connect existing components together. \n") 
        f.write("Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. \n")
        f.write("Python supports modules and packages, which encourages program modularity and code reuse.\n") 
        f.write("The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.\n")
        f.write("\n,\n")
        f.write("Title : What is Data Analysis ? \n")
        f.write("The process of evaluating data using analytical and logical reasoning to examine each component of the data provided. \n")
        f.write("This form of analysis is just one of the many steps that must be completed when conducting a research experiment.\n")
        f.write("Data from various sources is gathered, reviewed, and then analyzed to form some sort of finding or conclusion.\n")
        f.write("There are a variety of specific data analysis method, some of which include data mining, text analytics, business intelligence, and data visualizations. \n")
'''

# Below with will read the file and output it to the screen. Used for testing so I have commented it out.
'''
with open("Q9_File.txt", "r") as f:
    s = f.read()
print(s)
print("\n")
'''


#Below with statement is accepthing empty lines as I have added a space between the paragraphs. I will rewrite it below using .split
'''
with open("Q9_File.txt", "r") as f:
    count = 0
    for line in f:
        count += 1
        if count % 2 == 1:
            print(line)
'''

# Rewritten block of code to not include the line spacing on line 22. Please note that I have added a second line space into line 22 as I want line 23 to output. 
'''
with open("Q9_File.txt", "r") as f:
    count = 2                   # Set a variable to 2 that will used in the elif 
    for line in f:              # For loop used to increment count by one as it loops the file f
        count += 1              # Add 1 to count as it loops
        if not line.strip():    # If the line is empty continue will just pass it and not display it as output
            continue            # continue is used to skip the line if is contains while spaces
        elif count % 2 == 1:    # Used to indicate a remander and if it is 1 it will print that line
            print(line)        
'''


