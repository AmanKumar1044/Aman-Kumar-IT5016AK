class Car:
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

car1 = Car("black", "Tesla Model S", 2023)
print(car1.color, car1.model, car1.year)