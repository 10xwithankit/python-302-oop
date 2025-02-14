# Define the SuperHero class
class SuperHero:
    def __init__(self, name, superpower, origin):
        self.name = name
        self.superpower = superpower
        self.origin = origin

# Create an instance of the `SuperHero` class
hero1 = SuperHero("Green Lantern", "Power Ring", "Earth")

# Create another instance of the `SuperHero` class
hero2 = SuperHero("Cyborg", "Cybernetic Enhancements", "Detroit")

# Create another instance of the `SuperHero` class
hero3 = SuperHero("Martian Manhunter", "Shapeshifting", "Mars")

# Print the details of each superhero using f-string formatting
print(f"{hero1.name} - {hero1.superpower} ({hero1.origin})")  # Output: Green Lantern - Power Ring (Earth)
print(f"{hero2.name} - {hero2.superpower} ({hero2.origin})")  # Output: Cyborg - Cybernetic Enhancements (Detroit)
print(f"{hero3.name} - {hero3.superpower} ({hero3.origin})")  # Output: Martian Manhunter - Shapeshifting (Mars)
