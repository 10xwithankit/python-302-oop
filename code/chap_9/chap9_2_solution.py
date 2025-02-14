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

# Define a subclass `CreditCardPayment` that inherits from `Payment`
class CreditCardPayment(Payment):
    
    # Implement the `process_payment` method
    # This method prints a message for processing a credit card payment
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")

# Define another subclass `PayPalPayment` that inherits from `Payment`
class PayPalPayment(Payment):
    
    # Implement the `process_payment` method
    # This method prints a message for processing a PayPal payment
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")

# Create an instance of `CreditCardPayment`
cc_payment = CreditCardPayment()

# Call the `process_payment` method for `CreditCardPayment`
cc_payment.process_payment(100)  # Output: Processing credit card payment of $100
