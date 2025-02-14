# Define the SuperHero class as we did in previous exercise 
class SuperHero:
    def __init__(self, name, superpower, origin):
        self.name = name
        self.superpower = superpower
        self.origin = origin

# Create an instance of the `SuperHero` class
# `hero1` represents Superman with specific attributes
hero1 = SuperHero("Superman", "Super Strength", "Krypton")

# Create another instance of the `SuperHero` class
# `hero2` represents Wonder Woman with specific attributes
hero2 = SuperHero("Wonder Woman", "Combat Skills", "Themyscira")

# Print details of `hero1`
# Using f-strings to format the output dynamically
print(f"{hero1.name} has {hero1.superpower} and comes from {hero1.origin}.")
# Expected Output: Superman has Super Strength and comes from Krypton.

# Print details of `hero2`
# Using f-strings to format the output dynamically
print(f"{hero2.name} has {hero2.superpower} and comes from {hero2.origin}.")
# Expected Output: Wonder Woman has Combat Skills and comes from Themyscira.
