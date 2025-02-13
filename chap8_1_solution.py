# Define a class `Car`
class Car:
    
    # Define a class attribute `total_cars`
    # This keeps track of the total number of car instances created
    total_cars = 0  
    
    # Define the constructor method (__init__)
    # This method initializes the car's attributes
    def __init__(self, brand):
        
        # Assign the `brand` parameter to the instance variable `self.brand`
        self.brand = brand  
        
        # Increment the class attribute `total_cars` by 1 each time a new car is created
        Car.total_cars += 1  

    # Define a class method `get_total_cars`
    # This method returns the total number of car instances created
    @classmethod
    def get_total_cars(cls):
        return cls.total_cars  # Access the class attribute

# Create an instance of the `Car` class with brand "Toyota"
car1 = Car("Toyota")

# Create another instance of the `Car` class with brand "Honda"
car2 = Car("Honda")

# Print the total number of cars using the class method
print(Car.get_total_cars())  # Output: 2
