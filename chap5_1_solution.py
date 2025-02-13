# Define a class `Student`
class Student:
    
    # Define the constructor method (__init__)
    # This method initializes the student's attributes
    def __init__(self, name, age, grade):
        
        # Public attribute: Can be accessed directly from outside the class
        self.name = name  
        
        # Protected attribute: Conventionally meant to be used within the class or subclasses
        self._age = age  
        
        # Private attribute: Cannot be accessed directly outside the class
        self.__grade = grade  

# Create an instance of the `Student` class
student = Student("Alice", 20, "A")

# Accessing a public attribute directly (Allowed)
print(student.name)  # Works fine (Public)

# Accessing a protected attribute directly (Possible, but not recommended)
print(student._age)  # Possible, but not recommended (Protected)

# Accessing a private attribute directly (Raises AttributeError)
print(student.__grade)  # Raises AttributeError (Private)
