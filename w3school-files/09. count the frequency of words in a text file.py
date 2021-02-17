
# Write a Python program to count the frequency of words in a text file

word_freq = []
with open("file.txt","r") as file:
    for line in file:
        words = line.strip().lower().split(" ")
        print(words)
        for word in words:
            word_freq.append(words.count(word))

print("Pairs\n" + str(list(zip(words,word_freq))))
            





