

class Vehicle:
    def __init__(self,name, model, color):
        self.car_name = name
        self.car_model = model
        self.car_color = color

    def car_description(self):
        print("\nDescription of your car:\nCar Name : {}\nCAr Model : {}\nCar Color : {}".format(self.car_name, self.car_model, self.car_color))

class Bus(Vehicle):
    def __init__(self, name, model, color):
        super().__init__(name, model, color)

name = input("Name of your car : ")
model = input("Name of your car's model : ")
color = input("Color of your car : ")
car1 = Bus(name, model, color)
car1.car_description()