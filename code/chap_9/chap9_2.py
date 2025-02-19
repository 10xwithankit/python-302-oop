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
# This method prints a message for processing a credit card payment

# Define another subclass `PayPalPayment` that inherits from `Payment`

# Implement the `process_payment` method
# This method prints a message for processing a PayPal payment

# Define another subclass `BankTransferPayment` that inherits from `Payment`

# Implement the `process_payment` method
# This method prints a message for processing a bank transfer payment

# Create an instance of `CreditCardPayment` and process a payment

# Create an instance of `PayPalPayment` and process a payment

# Create an instance of `BankTransferPayment` and process a payment
