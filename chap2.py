class SuperHero:
    team = "Justice League"  # Class variable

    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level
    
    def attack(self):
        print(f"{self.name} attacks with power level {self.power_level}!")

# Creating hero objects
ww = SuperHero("Wonder Woman", 100)
bm = SuperHero("Batman", 90)

# Using hero abilities
ww.attack()
bm.attack()

# Printing class variable
print(SuperHero.team)
