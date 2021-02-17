
#Sort the dict. created according to marks.

n = int(input("Enter how many record wants to add? "))

class_list = {}

for _ in range(n):
    keys = input("Enter name: ")
    values = int(input("Enter marks: "))
    class_list[keys] = values

print("\nBefore sorting the Dictionary:")
print(class_list)

sorted_values = sorted(class_list.values())
sorted_class_list = {}
for i in sorted_values:
    for j in class_list.keys():
        if class_list[j] == i:
            sorted_class_list[j] = class_list[j]
            

print("\nAfter sorting the Dictionary:")
print(sorted_class_list)