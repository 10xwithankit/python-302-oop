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
class Car(Vehicle):
    
    # Define the constructor method (__init__) for `Car`
    # This method initializes the car's attributes, including fuel type
    def __init__(self, brand, speed, fuel_type):
        
        # Call the parent class constructor using `super()`
        super().__init__(brand, speed)  
        
        # Assign the `fuel_type` parameter to the instance variable `self.fuel_type`
        self.fuel_type = fuel_type  

    # Override the `move` method
    # This method calls the parent `move()` method and adds additional behavior
    def move(self):
        super().move()  # Call the `move()` method from `Vehicle`
        print("The car runs on", self.fuel_type)  # Additional message specific to `Car`

# Create an instance of the `Car` class
car = Car("Honda", 100, "Petrol")

# Call the overridden `move` method
car.move()
