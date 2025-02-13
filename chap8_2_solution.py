# Define a class `Car`
class Car:
    
    # Define a static method `is_valid_vin`
    # This method checks if a given VIN (Vehicle Identification Number) is valid
    @staticmethod
    def is_valid_vin(vin):
        # A valid VIN should have exactly 17 characters and be alphanumeric
        return len(vin) == 17 and vin.isalnum()

# Check if a VIN is valid using the static method
print(Car.is_valid_vin("1HGCM82633A123456"))  # Output: True

# Check if a short VIN is valid
print(Car.is_valid_vin("1234"))  # Output: False
