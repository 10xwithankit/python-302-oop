# Import the ABC module to define an abstract class
# Define an abstract class `Payment`
# Abstract classes cannot be instantiated and must be inherited by subclasses
# Define an abstract method `process_payment`
# This method must be implemented by any subclass

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass



# Define a subclass `CreditCardPayment` that inherits from `Payment`

# Implement the `process_payment` method
# This method returns a message for processing a credit card payment

# Define another subclass `PayPalPayment` that inherits from `Payment`

# Implement the `process_payment` method
# This method returns a message for processing a PayPal payment

# Create instances of `CreditCardPayment` and `PayPalPayment`

# Call the `process_payment` method for `CreditCardPayment` and `PayPalPayment`
