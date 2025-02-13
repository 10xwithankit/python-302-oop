# Define a class `AgeValidator`
class AgeValidator:
    
    # Define the constructor method (__init__)
    # This method initializes the person's age and validates it
    def __init__(self, age):
        
        # Check if the provided age is negative
        if age < 0:
            raise ValueError("Age cannot be negative!")  # Raise an exception if age is invalid
        
        # Assign the valid age to the instance variable
        self.age = age

# Use a try-except block to handle exceptions when creating an instance
try:
    # Attempt to create a `AgeValidator` object with a negative age
    person = AgeValidator(-5)  # This will raise a ValueError
except ValueError as e:
    # Catch and print the error message gracefully
    print(f"Error: {e}")
