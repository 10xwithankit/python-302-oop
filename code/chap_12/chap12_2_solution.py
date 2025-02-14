# Import `BaseModel` and `ValidationError` from the Pydantic library
from pydantic import BaseModel, ValidationError

# Define a class `User` that inherits from `BaseModel`
# Pydantic's `BaseModel` is used for data validation and modeling
class User(BaseModel):
    
    # Define attributes with type annotations
    first_name: str  # The user's first name must be a string
    last_name: str  # The user's last name must be a string

# Use a try-except block to handle validation errors
try:
    # Attempt to create an instance of `User` with incorrect data types
    invalid_user = User(first_name=123, last_name=True)  # This will raise a ValidationError
except ValidationError as e:
    # Catch and print the validation error in JSON format
    print(e.json())
