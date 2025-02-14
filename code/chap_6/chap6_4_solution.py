# Define a parent class `Vehicle`
class Vehicle:
    
    # Define a method `move`
    # This method prints a generic message indicating the vehicle is moving
    def move(self):
        print("The vehicle is moving.")

# Define a child class `Car` that inherits from `Vehicle`
class Car(Vehicle):
    
    # Override the `move` method
    # This method provides a specific implementation for a car
    def move(self):
        print("The car is driving on the road.")

# Define another child class `Boat` that also inherits from `Vehicle`
class Boat(Vehicle):
    
    # Override the `move` method
    # This method provides a specific implementation for a boat
    def move(self):
        print("The boat is sailing on water.")

# Create an instance of the `Car` class
car = Car()

# Create an instance of the `Boat` class
boat = Boat()

# Call the overridden `move` method for the `car` object
car.move()  # Output: The car is driving on the road.

# Call the overridden `move` method for the `boat` object
boat.move()  # Output: The boat is sailing on water.
