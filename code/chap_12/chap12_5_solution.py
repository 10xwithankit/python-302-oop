# Import necessary modules from Pydantic and Python's standard library
from pydantic import BaseModel, BeforeValidator
import datetime
from typing import Annotated

# Define a function `stamp2date`
# This function converts a Unix timestamp into a datetime object
def stamp2date(value):
    return datetime.datetime.fromtimestamp(value)

# Define a Pydantic model `DateModel`
# This model uses `BeforeValidator` to convert a timestamp into a datetime object
class DateModel(BaseModel):
    dob: Annotated[datetime.datetime, BeforeValidator(stamp2date)]

# Create an instance of `DateModel` with a Unix timestamp
user_dob = DateModel(dob=1700000000)  # Example timestamp

# Print the converted datetime object
print(user_dob)
