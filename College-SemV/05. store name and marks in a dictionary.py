
#Ask user to give name and marks of 10 students and store them in a dictionary.

n = int(input("Enter how many record wants to add? "))

class_list = {}

for _ in range(n):
    keys = input("Enter name: ")
    values = int(input("Enter marks: "))
    class_list[keys] = values

print("\nThe Dictionary:")
print(class_list)
