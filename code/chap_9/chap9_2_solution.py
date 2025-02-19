# Import the ABC module to define an abstract class
from abc import ABC, abstractmethod

# Define an abstract class `Payment`
# Abstract classes cannot be instantiated and must be inherited by subclasses
class Payment(ABC):
    
    # Define an abstract method `process_payment`
    # This method must be implemented by any subclass
    @abstractmethod
    def process_payment(self, amount):
        pass

# Define a subclass `CreditCardPayment` that inherits from `Payment`
class CreditCardPayment(Payment):
    
    # Implement the `process_payment` method
    # This method prints a message for processing a credit card payment
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")  # Output will now be printed

# Define another subclass `PayPalPayment` that inherits from `Payment`
class PayPalPayment(Payment):
    
    # Implement the `process_payment` method
    # This method prints a message for processing a PayPal payment
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")  # Output will now be printed

# Define another subclass `BankTransferPayment` that inherits from `Payment`
class BankTransferPayment(Payment):
    
    # Implement the `process_payment` method
    # This method prints a message for processing a bank transfer payment
    def process_payment(self, amount):
        print(f"Processing bank transfer payment of ${amount}")  # Output will now be printed

# Create an instance of `CreditCardPayment` and process a payment
cc_payment = CreditCardPayment()
cc_payment.process_payment(100)  # Output: Processing credit card payment of $100

# Create an instance of `PayPalPayment` and process a payment
paypal_payment = PayPalPayment()
paypal_payment.process_payment(50)  # Output: Processing PayPal payment of $50

# Create an instance of `BankTransferPayment` and process a payment
bank_payment = BankTransferPayment()
bank_payment.process_payment(200)  # Output: Processing bank transfer payment of $200
