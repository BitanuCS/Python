
# Creat a class sem 5 and creat object student. print the name and age of five students

class Sem5:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_record(self):
        print("\nDisplay the name and age of the students are:\n", dict(class_record))


class_record = []

n  = int(input("How many records wants to show?"))

while n != 0:
    stu_record = []
    name = input("What is your name? ")
    age = int(input("What is your age? "))
    while age < 1:
        age = int(input("What is your age? "))

    stu_record.append(name)
    stu_record.append(age)

    class_record.append(stu_record)
    
    n -=1

for i in class_record:
    student = Sem5(name, age)

student.show_record()
