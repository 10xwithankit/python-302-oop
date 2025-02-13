# Define a class `Engine`
class Engine:
    
    # Define the constructor method (__init__)
    # This method initializes the engine's horsepower
    def __init__(self, horsepower):
        self.horsepower = horsepower  # Set the engine's horsepower
    
    # Define a method `start`
    # This method prints a message indicating the engine has started
    def start(self):
        print("Engine started!")

# Define a class `Car`
class Car:
    
    # Define the constructor method (__init__)
    # This method initializes the car's brand and associates it with an engine
    def __init__(self, brand, horsepower):
        self.brand = brand  # Assign the car's brand
        self.engine = Engine(horsepower)  # Composition: Car has an Engine object
    
    # Define a method `drive`
    # This method starts the engine and prints a message indicating the car is driving
    def drive(self):
        self.engine.start()  # Start the engine
        print(f"{self.brand} is now driving!")

# Create an instance of `Car` with brand "Toyota" and engine power of 200 HP
my_car = Car("Toyota", 200)

# Call the `drive` method to start the car
my_car.drive()
