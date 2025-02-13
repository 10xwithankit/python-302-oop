# Import `BaseModel` from the Pydantic library
# Import `List` from the typing module to handle lists of objects
from pydantic import BaseModel
from typing import List

# Define a class `Address` that inherits from `BaseModel`
# This class represents an address with specific attributes
class Address(BaseModel):
    street: str  # The street address
    city: str  # The city name
    zip_code: str  # The postal ZIP code

# Define a class `User` that inherits from `BaseModel`
# This class represents a user with multiple addresses
class User(BaseModel):
    username: str  # The user's username
    addresses: List[Address]  # A list of address objects

# Create an instance of `User` with multiple addresses
user = User(
    username="john_doe",
    addresses=[
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
        {"street": "456 Elm St", "city": "Los Angeles", "zip_code": "90001"}
    ]
)

# Print the validated user object
print(user)
