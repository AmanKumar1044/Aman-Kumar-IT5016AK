class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
            print(f"The {self.color} {self.model} is driving.")

    def stop(self):
            print(f"The {self.color} {self.model} has stopped.")

car1 = Car("Blue","Ford Mustang")
car2 = Car("Blue","Ford Mustang", 2021)
car1.drive()
car1.stop()
print(f"car info: {self.year} {self.color} {self.model}")
