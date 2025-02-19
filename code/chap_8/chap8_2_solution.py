# Define a class `Validator`
class Validator:
    
    # Define a static method `is_valid_email`
    # This method checks if a given email is valid based on basic formatting rules
    @staticmethod
    def is_valid_email(email):
        # A valid email must contain "@" and at least one "." after the "@" symbol
        return "@" in email and "." in email.split("@")[1]

# Call the static method to validate email addresses
print(Validator.is_valid_email("test@example.com"))  # Output: True
print(Validator.is_valid_email("invalid-email"))  # Output: False
