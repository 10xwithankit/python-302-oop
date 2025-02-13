# Define a custom exception class `InsufficientFundsError`
class InsufficientFundsError(Exception):
    
    # Define the constructor method (__init__)
    # This method initializes the exception with a custom error message
    def __init__(self, balance, amount):
        # Use `super()` to call the parent Exception class constructor with a formatted message
        super().__init__(f"Attempted to withdraw ${amount} with only ${balance} available.")

# Define a class `BankAccount`
class BankAccount:
    
    # Define the constructor method (__init__)
    # This method initializes the bank account balance
    def __init__(self, balance):
        self.balance = balance  # Set the initial balance
    
    # Define a method `withdraw`
    # This method allows withdrawing money while handling insufficient funds
    def withdraw(self, amount):
        # Check if the withdrawal amount exceeds the available balance
        if amount > self.balance:
            # Raise the custom `InsufficientFundsError` exception
            raise InsufficientFundsError(self.balance, amount)
        
        # Deduct the amount from the balance
        self.balance -= amount
        return self.balance  # Return the updated balance

# Create an instance of `BankAccount` with an initial balance of 100
account = BankAccount(100)

# Use a try-except block to handle insufficient funds exception
try:
    # Attempt to withdraw 200 (insufficient funds)
    print(account.withdraw(200))
except InsufficientFundsError as e:
    # Catch and print the custom error message
    print(f"Transaction failed: {e}")
