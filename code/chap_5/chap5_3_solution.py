# Define a class `Person`
class Person:
    
    # Define the constructor method (__init__)
    # This method initializes the person's attributes
    def __init__(self, name, age):
        
        # Public attribute: Can be accessed directly
        self.name = name  
        
        # Private attribute: Cannot be accessed directly outside the class
        self.__age = age  

    # Define a getter method using @property
    @property
    def age(self):  
        return self.__age  

    # Define a setter method using @age.setter
    @age.setter
    def age(self, new_age):
        self.__age = new_age  # Update the age
        

# Create an instance of the `Person` class
person = Person("Alice", 25)

# Access age using the getter
print(person.age)  # ✅ Output: 25 (No parentheses needed!)

# Update age using the setter
person.age = 30  # ✅ Uses setter method
print(person.age)  # ✅ Output: 30


