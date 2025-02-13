# Define a class `Person`
# Define the constructor method (__init__)
# This method initializes the person's attributes
# Public attribute: Can be accessed directly

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private Attribute


# Private attribute: Cannot be accessed directly outside the class

# Define a setter method `set_age`
# This method allows controlled modification of the private attribute `__age`

# Check if the new age is a positive number
# Update the age if the condition is met
# Print an error message if invalid

# Define a getter method `get_age`
# This method provides controlled access to the private attribute `__age`

# Create an instance of the `Person` class

# Update age using the setter method

# Retrieve the updated age using the getter method

# Attempt to set an invalid age (negative number)
