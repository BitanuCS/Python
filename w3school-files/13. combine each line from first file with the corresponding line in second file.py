
# Write a Python program to combine each line from first file with the corresponding line in second file

file3 = open("final_file.txt","w")
with open("file.txt","r") as file1, open("file1.txt","r") as file2:
    for f_1, f_2 in zip(file1, file2):
        f_3 = f_1 + f_2
        file3.writelines(f_3)

file3.close()
print(open("final_file.txt","r").read())
