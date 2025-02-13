# Import `BaseModel`, `validator`, and `EmailStr` from the Pydantic library
from pydantic import BaseModel, validator, EmailStr

# Define a class `User` that inherits from `BaseModel`
# This class represents a user with validation rules
class User(BaseModel):
    name: str  # The user's name
    age: int  # The user's age
    email: EmailStr  # The user's email (validated as a proper email format)

    # Define a validator for the `age` field
    # This method ensures that the user's age is at least 18
    @validator("age")
    def validate_age(cls, value):
        if value < 18:
            raise ValueError("Age must be at least 18")  # Raise an error if age is below 18
        return value  # Return the valid age
