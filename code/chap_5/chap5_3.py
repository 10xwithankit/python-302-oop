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
    
        

# Update age using the setter


