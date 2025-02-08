class Car:
    def __init__(self, brand, color):
        self.brand = brand  # Attribute: Brand of the car
        self.color = color  # Attribute: Color of the car
    
    def drive(self):  # Method: What the car can do
        print(f"The {self.color} {self.brand} is driving!")
