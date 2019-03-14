## Course : Higher Diploma in Science in Computing in Data Analytics
## Module : Programming and Scripting


# Problem Set 2019

This document contains the instructions for Problem Set 2019 for Programming and Scripting.
Please find a link below to the problem set that we are required to complete

        https://github.com/ianmcloughlin/problems-pands-2019/raw/master/problems.pdf

## How to run these files 
   * Download and install anaconda on your device ( I recommend version 3.7 +) 
   * Download and install Visual Studio Code 
   * Download Cmder command line (optional)
   * Go to my repository https://github.com/richardfeeney7/Problem_Sets
   * Once the repository is open click on the green clone/download button and download zip
   * Save this zip file on your local machine
   * Open Cmder or Anaconda command prompt
   * Navigate to the directory when you have unzipped the my repository
   * On the command line write python problem_1.py to open the first problem, python problem_2 for the next etc

## Question 1

*Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_1.py


This program will request the user to input a positive number. Once the number is entered it will get the total sum between 1 and the user input. An example for this would be if the number nine was entered the result displayed back to the user is forty-five. I have also added in the option for the user to try again or exit the application. If a negative number is entered the user will be notified that they cant use a negative number and if they would like to try again. To create this application I have used a function that will accept the number entered by the user. I then used while loops and if statements to generate the required result. 

*Additional study resources used*
    
    * https://www.w3schools.com/python/python_while_loops.asp

    * https://www.tutorialspoint.com/python/python_while_loop.htm

    * https://www.w3schools.com/python/python_variables.asp

    * https://www.w3schools.com/python/python_conditions.asp

## Question 2

*Write a program that outputs whether or not today is a day that begins with the letter T.*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_2.py


This program checks the current day and if it begins with the letter T. If the day falls on a Tuesday or Thursday it will output to the user that today begins with the letter T. If the day begins with any other letter the user will be notified what the current day is and that it does not start with the letter T. To create this application I imported the datetime function and gave it an alias of dt. I then used datetime.now() to get the current time and date and store it in a variable that I will use in an IF statement to check if the day begins with the letter T. I have also used the string format time function (strftime("")) to return the string that will output the current day. 


*Additional study resources used*

    * https://www.youtube.com/watch?v=eirjjyP2qcQ

    * https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python

    * https://www.programiz.com/python-programming/datetime/strftime

## Question 3

*Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_3.py


This program will display all the number that are divisible by six. To complete this question I used a for loop with a range function that started at 1000 and finished at 10001. The extra one to ten thousand was required so ten thousand would also be included. In the FOR loop I have user an IF statement to find what is divisible by six but not twelve. If the number is divisible by both six and twelve the line will be skipped and wont be outputted for the user to see. 


*Additional study resources used*

    * https://www.digitalocean.com/community/tutorials/ how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3

    * https://www.w3schools.com/python/ref_func_range.asp


## Question 4

*Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and,if it is even divide it by two,but if it is odd,multiply it by three and add one. Have the program end if the current value is one.*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_4.py


To complete this question I have used a WHILE loop and and two IF statement. One of the IF statements will be executed if the user enters a number less than one and they will be asked to try again. 

The second IF statement is contained within the WHILE loop and will check if the current value in the loop is even and if it is it will be divided by two. The ELSE to this IF statement will be executed if the number is odd and in this case it will be multiplied by three with one added to it.


*Additional study resources used*

    * https://www.youtube.com/watch?v=5mFpVDpKX70

    * https://math.stackexchange.com/questions/2694/what-is-the-importance-of-the-collatz-conjecture


## Question 5

*Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime*   


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_5.py


Completed this question by using a FOR Loop and range function that is inside an IF statement that will be executed if the input is greater than one otherwise idf the input is one or less the used will be told to try again. Another IF statement inside the FOR Loop checks if the the input has a remainder of 0 / divides by two. If it can divide by two it is not a prime number. 

*Additional study resources used*

    * https://www.pythoncentral.io/pythons-range-function-explained/? fbclid=IwAR2ybMGVtGGxXdW-e3FMYh6OLgwB9jkSjej-Igr96Bz6581hl1s0xSaILZI

    * https://stackoverflow.com/questions/11619942/print-series-of-prime-numbers-in-python?fbclid=IwAR0oTLdlnxyIj0bdKz_gqOJWTJr2m2LnkICzHVtzemMlNt_ie80KR-nvI04


## Question 6

*Write a program that takes a user input string and outputs every second word.* 


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_6.py


By using .split() I can take the input and put it into a list. I can then slice this list to retrieve the information that i need. I used len() in the slice so it will jump in multiples of two depending on the string length the user provided. 

I have used * at the beginning of the slice as this stopped [ ] appearing when every second work was printed out on screen. I could have used .join in my slice instead of * but * was quicker for me. 


*Additional study resources used*

    * https://www.youtube.com/watch?v=ajrtAuDg3yw

    * https://www.w3schools.com/python/ref_string_split.asp
    
    * https://www.decalage.info/en/python/print_list

    * https://www.w3schools.com/python/ref_string_replace.asp


## Question 7

*Write a program that takes a positive ﬂoating point number as input and outputs an approximation of its square root.*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_7.py


Python has a module called math that stores a functions sqrt() which I have used to complete this question. I added in an IF ELSE statement to verify if the input was a positive number and display the answer on the screen. If the user entered a negative number they will be asked to input a positive number. I have used the round function as part of my print statement and set this to two decimal places.


*Additional study resources used*

    * https://www.tutorialspoint.com/python/number_sqrt.htm
    * https://www.w3schools.com/python/ref_func_round.asp


## Question 8

*Write a program that outputs today’s date and time in the format “Monday,January 10th 2019 at 1:15pm”.*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_8.py


To complete this question I first imported the datetime module and then created a variable that will store the current date and time. To find the date and time as specified in the question I used the strftime module to pull the required information and formatting from datetime. 


*Additional study resources used*

    * https://www.journaldev.com/23324/python-strftime
    * https://docs.python.org/2/library/datetime.html


## Question 9

*Write a program that reads in a text ﬁle and outputs every second line.*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_9.py


In this question I have used the with keyword as this will automatically close file once it is finished. I used f.write to save the lines of code to a separate TXT file that will be used to pull the information and print every second line. 

When displaying the output I set a alias for my TXT file. I then created a variable that will increment by one as it loops through a FOR loop. The FOR loop is used with an IF statement inside it to check i and if it will be displayed or skipped. The application was displaying blank lines as output and to stop this from happening I used line.strip(), this will remove all white spaces


*Additional study resources used*

    * https://stackoverflow.com/a/40647980/5644281m
    * https://docs.python.org/2/tutorial/inputoutput.html
    * https://www.tutorialspoint.com/python/string_strip.htm
    

## Question 10

*Write a program that displays a plot of the functions x, x2 and 2x in the range [0,4].*


Please follow this link to view the finished python code : https://github.com/richardfeeney7/Problem_Sets/blob/master/Problem_10.py


In this question I have used the with keyword as this will automatically close file once it is finished. I used f.write to save the lines of code to a separate TXT file that will be used to pull the information and print every second line. 

When displaying the output I set a alias for my TXT file. I then created a variable that will increment by one as it loops through a FOR loop. The FOR loop is used with an IF statement inside it to check i and if it will be displayed or skipped. The application was displaying blank lines as output and to stop this from happening I used line.strip(), this will remove all white spaces


*Additional study resources used*

    * https://www.tutorialspoint.com/python/python_matplotlib.htm