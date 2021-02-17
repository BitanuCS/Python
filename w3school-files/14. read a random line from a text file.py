
# Write a Python program to read a random line from a file

import random
with open("file.txt","r") as file1:
    print(random.choice(file1.read().splitlines()))

file1.close()
