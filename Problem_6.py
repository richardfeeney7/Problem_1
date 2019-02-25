#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 6 :    
#           Write a program that takes a user input string and outputs every second word?


sent = input("Please enter a sentence : ").split() # Accept user input and store in sent
# Split is used to split the string into a list


#     sent[start:end:step] 
print(*sent[1:len(sent):2], sep=" ---- ") #slicing the string to pull the information needed. len () will 
# sep is used to add a seperation with lines between the work. Not needed but I think it reads better


# To remove [] from the output I have added a * just before sent in the pint statement but the statement
# using the .join does the same thing and puts a comma between the words.
# print (', '.join(sent[1:len(sent):2]))
