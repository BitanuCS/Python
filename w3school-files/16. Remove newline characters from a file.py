
# Write a Python program to remove newline characters from a file

with open("file.txt","r") as file1:
    file1 = file1.readlines()
    print([f.rstrip("\n") for f in file1])