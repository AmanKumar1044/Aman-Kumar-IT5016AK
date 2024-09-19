class Car():
    def _init_(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    def drive(self):
        print(F"The {self.color} {self.model} is driving.")
   
    def stop(self):    
        print(F"The {self.color} {self.model} has stopped.")

    def display_info(self):
        print(F"Car Info: {self.year} {self.color} {self.model} ")

class Electric_car(Car):
    def _init_(self, color, model, year, batterycapacity):
        super()._init_(color, model, year)
        self.batterycappacity = batterycapacity

    def display_info(self):
        super().display_info()    
        print(F"Battery Capacity:{self.batterycappacity}kwh")


car1 = Electric_car("Tesla","Black",2024,75)
car1.drive()
car1.stop()
car1.display_info()     


