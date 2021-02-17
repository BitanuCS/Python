
# Write a Python program to read a file line by line and store it into a list

list = []

with open("file.txt","r") as file:
    list = file.readlines()

print(list)
