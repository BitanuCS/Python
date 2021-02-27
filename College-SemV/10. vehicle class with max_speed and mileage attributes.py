
# creat a vehicle class with max_speed and mileage attributes.

class Vehicle:
    def __init__(self,max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        print("Max. Speed of your car is: {}\nMileage is: {}".format(max_speed,mileage))


max_speed = float(input("What is the max_speed of your car? "))
mileage = float(input("What is the mileage of your car? "))

car = Vehicle(max_speed,mileage)