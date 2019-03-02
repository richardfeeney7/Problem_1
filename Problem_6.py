#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 6 :    
#           Write a program that takes a user input string and outputs every second word?


sent = input("Please enter a sentence : ").split(' ') # Accept user input and store in sent & Split is used to split the string into a list

sent = [ignore.replace(',',  '').replace('.' , '') for ignore in sent] # This lne of code will ignore input of , & . 

      #sent[start:end:step] How to slice the string sent. 
print(*sent[0:len(sent):2], sep=" / ",) # Slicing the string to pull the information needed. 
                                        # ep is used to add a / between words. 
                                        # To remove [] from the output I have added a * just before sent in the pint statement
# Using the .join does the same thing and puts a comma between the words.
# Print (', '.join(sent[1:len(sent):2]))
