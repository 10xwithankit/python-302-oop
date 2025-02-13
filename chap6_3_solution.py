# Define a class `Engine`
class Engine:
    
    # Define a method `start_engine`
    # This method prints a message indicating the engine has started
    def start_engine(self):
        print("Engine started!")

# Define a class `Wheels`
class Wheels:
    
    # Define a method `move_wheels`
    # This method prints a message indicating the wheels are moving
    def move_wheels(self):
        print("Wheels moving!")

# Define a class `Car` that inherits from both `Engine` and `Wheels`
# This is an example of multiple inheritance
class Car(Engine, Wheels):
    pass  # Inherits all methods from both parent classes

# Create an instance of the `Car` class
my_car = Car()

# Call the `start_engine` method inherited from `Engine`
my_car.start_engine()  # Output: Engine started!

# Call the `move_wheels` method inherited from `Wheels`
my_car.move_wheels()  # Output: Wheels moving!
