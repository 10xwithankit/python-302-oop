# Import necessary modules from Pydantic and Python's standard library
from pydantic import BaseModel, BeforeValidator
import datetime
from typing import Annotated

# Define a function `stamp2date`
# This function converts a timestamp into a datetime object
def stamp2date(value):
    return datetime.datetime.fromtimestamp(value)

# Define a class `DateModel` that inherits from `BaseModel`
# This class represents a model with a validated date of birth field
class DateModel(BaseModel):
    # Use `Annotated` to specify that `dob` will be converted using `BeforeValidator`
    dob: Annotated[datetime.datetime, BeforeValidator(stamp2date)]
