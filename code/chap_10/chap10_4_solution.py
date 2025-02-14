# Define a class `Temperature`
class Temperature:
    
    # Define the constructor method (__init__)
    # This method initializes the temperature in Celsius and validates it
    def __init__(self, celsius):
        
        # Check if the provided temperature is below absolute zero (-273.15°C)
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero is not possible!")  # Raise an exception if temperature is invalid
        
        # Assign the valid temperature to the instance variable
        self.celsius = celsius

# Use a try-except block to handle exceptions when creating an instance
try:
    # Attempt to create a `Temperature` object with an invalid value (-500°C)
    t = Temperature(-500)  # This will raise a ValueError
except ValueError as e:
    # Catch and print the error message gracefully
    print(f"Error: {e}")
