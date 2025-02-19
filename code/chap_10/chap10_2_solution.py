# Define a class `AgeValidator`
class AgeValidator:
    
    # Define the constructor method (__init__)
    # This method initializes the age and applies validation checks
    def __init__(self, age):
        
        # Check if the provided age is not an integer
        if not isinstance(age, int):
            raise TypeError("Age must be an integer!")  # Raise a TypeError if age is not an integer
        
        # Check if the provided age is negative
        if age < 0:
            raise ValueError("Age cannot be negative!")  # Raise a ValueError if age is below 0
        
        # Check if the provided age exceeds a realistic limit (150 years)
        if age > 100:
            raise ValueError("Age cannot be greater than 100!")  # Raise a ValueError if age is above 150
        
        # Assign the validated age to the instance variable
        self.age = age

# Use a try-except block to handle exceptions when creating instances

# Attempt to create an `AgeValidator` object with a non-integer value ("twenty")
try:
    person = AgeValidator("twenty")  # Raises a TypeError
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Attempt to create an `AgeValidator` object with a negative age (-5)
try:
    person = AgeValidator(-5)  # Raises a ValueError
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# Attempt to create an `AgeValidator` object with an unrealistic age (200)
try:
    person = AgeValidator(200)  # Raises a ValueError
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
