# Define a class `Person`
class Person:
    
    # Define the constructor method (__init__)
    # This method initializes the person's attributes
    def __init__(self, name, age):
        
        # Public attribute: Can be accessed directly
        self.name = name  
        
        # Private attribute: Cannot be accessed directly outside the class
        self.__age = age  

    # Define a getter method `get_age`
    # This method provides controlled access to the private attribute `__age`
    @property
    def get_age(self):
        return self.__age  

# Create an instance of the `Person` class
person = Person("Alice", 25)

# Accessing the private attribute using the getter method
print(person.get_age())  # Output: 25
