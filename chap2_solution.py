# Define a class SuperHero:
#   - create instance variables - name, power_level
#   - create method(s):
#       - attack: prints "{name} attacks with power level {power_level}!"


class SuperHero:
    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def attack(self):
        print(f"{self.name} is on power level {self.power_level}!")


# Creating hero objects
ww = SuperHero("Wonder Woman", 100)
bm = SuperHero("Batman", 90)

# Use hero abilities
ww.attack()
bm.attack()
