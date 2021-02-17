
# Write a Python program to read an entire text file.

file = open("file.txt","r")
lines = file.readlines()
for line in lines:
    print(line)

file.close()