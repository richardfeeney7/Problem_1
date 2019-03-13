#                   Author : Richard Feeney Started: 25/02/2019

#                                    Problem 6 :    
#           Write a program that takes a user input string and outputs every second word?


sent = input("Please enter a sentence : ").split(' ') # Accept user input and store in sent & Split is used to break the string into a list

sent = [ignore.replace(',',  '').replace('.' , '') for ignore in sent] # This line of code is used to ignore input of " , & ."  in the user input that is stored in sent. 

      #sent[start:end:step] How to slice the string sent. 
print(*sent[0:len(sent):2], sep=" / ",) # Slicing the string to pull the information needed. 
                                        # sep is used to add a / between words, just for easier reading 
                                        # To remove [] from the output I have added a * just before sent in the pint statement

'''
In the print statement on line 12 we can use ".join" either, the code for this is below.
print (', '.join(sent[1:len(sent):2]))
'''