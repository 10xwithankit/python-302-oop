# Import the ABC module to define an abstract class
from abc import ABC, abstractmethod

# Define an abstract class `Payment`
# Abstract classes cannot be instantiated and must be inherited by subclasses
class Payment(ABC):
    
    # Define an abstract method `process_payment`
    # This method must be implemented by any subclass
    @abstractmethod
    def process_payment(self, amount):
        pass  # No implementation in the abstract class
