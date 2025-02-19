# Import the ABC module to define an abstract class
# Define an abstract class `Payment`
# Define an abstract method `process_payment`
from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract Class
    @abstractmethod
    def process_payment(self, amount):
        pass  # No implementation here


# Define a subclass `CreditCardPayment` that inherits from `Payment`
class CreditCardPayment(Payment):
    
    # Implement the `process_payment` method
    # This method returns a message for processing a credit card payment
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

# Define another subclass `PayPalPayment` that inherits from `Payment`
class PayPalPayment(Payment):
    
    # Implement the `process_payment` method
    # This method returns a message for processing a PayPal payment
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"

# Create instances of `CreditCardPayment` and `PayPalPayment`
cc_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Call the `process_payment` method for `CreditCardPayment` and `PayPalPayment`
output1 = cc_payment.process_payment(100)  # Should return a valid output
output2 = paypal_payment.process_payment(50)  # Should return a valid output
