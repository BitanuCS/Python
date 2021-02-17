
# Write a Python program to write a list to a text file

bag = ["applet","bug","c","django","ethernet","file"]

with open("list_container","w") as file:
    for l in bag:
        file.write("%s\n" % l)

print(open("list_container","r").read())
file.close()