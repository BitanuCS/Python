
# Write a python program to find the longest word in a text file

with open("file.txt","r") as file:
    long_word = ""
    for word in file.read().split():
        # print(word)
        if (len(word) > len(long_word)):
            long_word = word


print(long_word)
file.close()