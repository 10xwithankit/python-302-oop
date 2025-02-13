# Define a parent class `Vehicle`
class Vehicle:
    
    # Define the constructor method (__init__)
    # This method initializes the vehicle's attributes
    def __init__(self, brand, speed):
        
        # Assign the `brand` parameter to the instance variable `self.brand`
        self.brand = brand  
        
        # Assign the `speed` parameter to the instance variable `self.speed`
        self.speed = speed  

    # Define a method `move`
    # This method prints the movement details of the vehicle
    def move(self):
        print(f"{self.brand} is moving at {self.speed} km/h")

# Define a child class `Car` that inherits from `Vehicle`
# Since it does not define any new methods or attributes, it inherits everything from `Vehicle`
class Car(Vehicle):
    pass  # Inherits all methods and attributes from `Vehicle`

# Define another child class `Bicycle` that also inherits from `Vehicle`
class Bicycle(Vehicle):
    pass  # Inherits all methods and attributes from `Vehicle`

# Create an instance of the `Car` class
# This object inherits properties from `Vehicle`
car = Car("Toyota", 120)

# Create an instance of the `Bicycle` class
# This object also inherits properties from `Vehicle`
bike = Bicycle("Giant", 25)

# Call the `move` method for the car object
car.move()  # Output: Toyota is moving at 120 km/h

# Call the `move` method for the bike object
bike.move()  # Output: Giant is moving at 25 km/h
