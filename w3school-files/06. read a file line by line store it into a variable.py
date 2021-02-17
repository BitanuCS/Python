
# Write a Python program to read a file line by line store it into a variable.

with open("file.txt","r") as file:
    line = file.readlines()
    print(line)

file.close()