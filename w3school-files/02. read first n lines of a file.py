
# Write a Python program to read first n lines of a file.

from itertools import islice

file = open("file.txt","r")

for line in islice(file,2): 
    print(line)

file.close()