#f = open("Q9_File.txt", "r") # Open the TXT file
#f = open("Q9_File.txt", "w") # Write to the TXT file. This will overwrite what is in the file already. 
#f = open("Q9_File.txt", "a") # Use a instead of w to not overwrite it but instead append the file.
#f = open("Q9_File.txt", "r+") # Read and write to a file
#s = f.read() # Read the file

# f.write ("Example how to write to \r\n a file") # Write to the file with some on a new line

#print(s)

#f.close()  # Close the File, not required but it is good practice


#Below with will write the text to the file
with open("Q9_File.txt", "w") as f: #recommended way to use as it will close once the indent finishes.
    f.write("TITLE  :  What is Python \n")
    f.write("Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. \n")
    f.write("Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as ascripting or glue language to connect existing components together. \n") 
    f.write("Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. \n")
    f.write("Python supports modules and packages, which encourages program modularity and code reuse.\n") 
    f.write("The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms, and can be freely distributed.\n")


#Below with will read the file and output it to the screen
with open("Q9_File.txt", "r") as f:
    s = f.read()
print(s)
print("\n")
print("\n")
print("\n")
with open("Q9_File.txt", "r") as f:
    count = 0
    for line in f:
        count += 1
        if count % 2 == 1:
            print(line)
