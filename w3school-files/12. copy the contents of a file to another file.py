
# Write a Python program to copy the contents of a file to another file

with open("one.txt","r") as file1, open("two.txt","a") as file2:
    for line in file1:
        file2.write("\n" + line)

print(open("two.txt").read())
