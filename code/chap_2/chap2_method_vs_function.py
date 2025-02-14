
def greet():
    print("Hello, welcome!")  # Function

class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}!")  # Method

# Using function
greet()

# Creating object and calling method
p = Person("Alice")
p.say_hello()
