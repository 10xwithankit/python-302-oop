# Define a class `SuperHero`
# A class is a blueprint for creating objects with specific attributes and behaviors
class SuperHero:
    
    # Define the constructor method (__init__)
    # This method is called automatically when a new object of the class is created
    def __init__(self, name, superpower, origin):
        
        # Assign the `name` parameter to the instance variable `self.name`
        # This stores the superhero's name in the object
        self.name = name  
        
        # Assign the `superpower` parameter to the instance variable `self.superpower`
        # This represents the superhero's special ability
        self.superpower = superpower  
        
        # Assign the `origin` parameter to the instance variable `self.origin`
        # This defines where the superhero comes from
        self.origin = origin  
