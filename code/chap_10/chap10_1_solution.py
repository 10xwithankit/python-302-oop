# Define a class `BankAccount`
class BankAccount:
    
    # Define the constructor method (__init__)
    # This method initializes the bank account balance
    def __init__(self, balance):
        self.balance = balance  # Set the initial balance
    
    # Define a method `withdraw`
    # This method allows withdrawing money while handling errors
    def withdraw(self, amount):
        try:
            # Check if the withdrawal amount exceeds the available balance
            if amount > self.balance:
                raise ValueError("Insufficient funds!")  # Raise an exception if insufficient funds
            
            # Deduct the amount from the balance
            self.balance -= amount
            return self.balance  # Return the updated balance
        
        except ValueError as e:
            # Gracefully handle the error and print an error message
            print(f"Error: {e}")  
            return self.balance  # Return the unchanged balance

# Create an instance of `BankAccount` with an initial balance of 100
account = BankAccount(100)

# Attempt to withdraw 50 (successful transaction)
print(account.withdraw(50))  # Output: 50

# Attempt to withdraw 200 (insufficient funds)
print(account.withdraw(200))  # Output: Error: Insufficient funds!
