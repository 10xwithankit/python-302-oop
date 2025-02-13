# Define a class `Person`
class Person:
    
    # Define the constructor method (__init__)
    # This method initializes the person's attributes
    def __init__(self, name, age):
        
        # Public attribute: Can be accessed directly
        self.name = name  
        
        # Private attribute: Cannot be accessed directly outside the class
        self.__age = age  

    # Define a setter method `set_age`
    # This method allows controlled modification of the private attribute `__age`
    def set_age(self, new_age):
        # Check if the new age is a positive number
        if new_age > 0:
            self.__age = new_age  # Update the age if the condition is met
        else:
            print("Age must be a positive number!")  # Print an error message if invalid

    # Define a getter method `get_age`
    # This method provides controlled access to the private attribute `__age`
    def get_age(self):
        return self.__age  

# Create an instance of the `Person` class
person = Person("Alice", 25)

# Update age using the setter method
person.set_age(30)  # Updates age to 30

# Retrieve the updated age using the getter method
print(person.get_age())  # Output: 30

# Attempt to set an invalid age (negative number)
person.set_age(-5)  # Output: Age must be a positive number!
