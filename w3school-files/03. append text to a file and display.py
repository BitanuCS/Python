
# Write a Python program to append text to a file and display the text.

file = open("file1.txt","a")

file.write("\n\nIt's nice\nYeah!")


with open("file1.txt") as file:
    for line in file:
        print(line.strip())
        
file.close()