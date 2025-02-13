# Define a custom exception class `InsufficientFundsError`

# Define the constructor method (__init__)
# This method initializes the exception with a custom error message

# Use `super()` to call the parent Exception class constructor with a formatted message

# Define a class `BankAccount`

# Define the constructor method (__init__)
# This method initializes the bank account balance

# Define a method `withdraw`
# This method allows withdrawing money while handling insufficient funds

# Check if the withdrawal amount exceeds the available balance
# Raise the custom `InsufficientFundsError` exception

# Deduct the amount from the balance
# Return the updated balance

# Create an instance of `BankAccount` with an initial balance of 100

# Use a try-except block to handle insufficient funds exception

# Attempt to withdraw 200 (insufficient funds)

# Catch and print the custom error message
