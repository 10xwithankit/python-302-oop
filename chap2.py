# Define a class SuperHero:
#   - create instance variables - name, power_level
#   - create method(s):
#       - attack: prints "{name} attacks with power level {power_level}!"
class SuperHero:
    name: str
    power_level: int

    def __init__(self, name, power_level):
        self.name = name
        self.power_level = power_level

    def attack(self):
        print(f"{self.name} attacks with power level {self.power_level}!")


# Instantiate 2 hero objects
ww = SuperHero("Wonder Woman", 100)
bm = SuperHero("Batman", 90)

# Print hero names and their power_level (for each objects)
print(ww.name, ww.power_level)
print(bm.name, bm.power_level)

# Call attack method for each obejct
ww.attack()
bm.attack()
