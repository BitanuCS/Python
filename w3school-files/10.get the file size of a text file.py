
# Write a Python program to get the file size of a text file

import os

file_stat = os.stat("/media/bitanu/Proramming/python/sample") #stat only take the file path
file_size = file_stat.st_size


print(file_stat)
print("File Size in Bytes is : {}" .format(file_size))
print("File Size in MegaBytes is : {}" .format(file_stat.st_size / (1024 * 1024)))
