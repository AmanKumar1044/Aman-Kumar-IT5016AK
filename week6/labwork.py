class Sportsperson():
    def __init__(self, name, age, nation, role):
        self.name = name
        self.age = age
        self.nation = nation
        self.role = role

    def Sports(self):
        cricket = input(f"which game the {self.name} is playing:")
        print(cricket)


cricketer1 = Sportsperson("Virat Kohli", 36 , "India",     "Batsman")
cricketer2 = Sportsperson("Messi", 34 ,     "Argentina",     "Attacker")

cricketer1.Sports()
cricketer2.Sports()
print(cricketer1.name, cricketer1.age, cricketer1.nation, cricketer1.role,)
print(cricketer2.name , cricketer2.age ,cricketer2.nation, cricketer2.role) 



