
# Write a Python program to count the number of lines in a text file

with open("file.txt","r") as file:
    count = 0
    letters = file.read().split("\n")
    for letter in letters:
        if letter:
            count +=1

print("Line No. : {}".format(count))
file.close()