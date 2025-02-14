# Define a class `SuperHero`
class SuperHero:
    
    # Define the constructor method (__init__)
    # This method initializes the attributes of the superhero
    # The `origin` parameter has a default value of "Unknown"
    def __init__(self, name, superpower, origin="Unknown"):
        
        # Assign the `name` parameter to the instance variable `self.name`
        self.name = name  
        
        # Assign the `superpower` parameter to the instance variable `self.superpower`
        self.superpower = superpower  
        
        # Assign the `origin` parameter to the instance variable `self.origin`
        # If no origin is provided, it defaults to "Unknown"
        self.origin = origin  

# Create an instance of the `SuperHero` class with only two arguments
# `hero1` represents Batman, and since no origin is provided, it defaults to "Unknown"
hero1 = SuperHero("Batman", "Genius Intellect")

# Create another instance of the `SuperHero` class with all three arguments
# `hero2` represents Aquaman, with "Atlantis" as the specified origin
hero2 = SuperHero("Aquaman", "Water Control", "Atlantis")

# Print the `origin` of `hero1`
# Since no origin was provided, it defaults to "Unknown"
print(hero1.origin)  # Output: Unknown

# Print the `origin` of `hero2`
# The origin was explicitly set to "Atlantis"
print(hero2.origin)  # Output: Atlantis
