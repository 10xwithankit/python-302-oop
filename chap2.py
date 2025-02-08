class SuperHero:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level
    
    def attack(self):
        print(f"{self.name} attacks with power level {self.power_level}!")

class FlyingSuperHero(SuperHero):
    def __init__(self, name, power_level, flight_speed):
        super().__init__(name, power_level)
        self.flight_speed = flight_speed
    
    def fly(self):
        print(f"{self.name} flies at speed {self.flight_speed}!")

# Creating hero objects
ww = SuperHero("Wonder Woman", 100)
bm = SuperHero("Batman", 90)
superman = FlyingSuperHero("Superman", 120, 500)

# Using hero abilities
ww.attack()
bm.attack()
superman.attack()
superman.fly()
