# Define a class SuperHero:
#   - create instance variables - name, power_level
#   - create method(s):
#       - attack: prints "{name} attacks with power level {power_level}!"


class SuperHero:
    name: str
    power_level: int

    def __init__(self, n, p_level):
        self.name = n
        self.power_level = p_level

    def attack(self):
        print(f"{self.name} attacks with power level {self.power_level}!")


# Instantiate 2 hero objects
ww = SuperHero("Wonder Woman", 100)
bm = SuperHero("Batman", 90)


# Print hero names and their power_level (for each objects)
print(f"Super Hero name is {ww.name} and power level is {ww.power_level}")
print(f"Super Hero name is {bm.name} and power level is {bm.power_level}")


# Call attack method for each obejct
ww.attack()
bm.attack()
