# Import the `BaseModel` class from the Pydantic library
from pydantic import BaseModel

# Define a class `User` that inherits from `BaseModel`
# Pydantic's `BaseModel` is used for data validation and modeling
class User(BaseModel):
    
    # Define attributes with type annotations
    first_name: str  # The user's first name
    last_name: str  # The user's last name

# Create an instance of `User` with valid data
valid_user = User(first_name="Marc", last_name="Nealer")

# Print the validated user object
print(valid_user)
