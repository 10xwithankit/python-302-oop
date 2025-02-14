# Define a parent class `Animal`
class Animal:
    
    # Define a method `breathe`
    # This method prints a message indicating the animal is breathing
    def breathe(self):
        print("Breathing...")

# Define a child class `Dog` that inherits from `Animal`
class Dog(Animal):
    
    # Define a method `bark`
    # This method prints a message indicating the dog is barking
    def bark(self):
        print("Woof!")

# Create an instance of the `Dog` class
buddy = Dog()

# Call the `breathe` method from the parent class `Animal`
buddy.breathe()  # Output: Breathing...

# Call the `bark` method defined in the `Dog` class
buddy.bark()  # Output: Woof!
