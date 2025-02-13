# Import the ABC module to define an abstract class
from abc import ABC, abstractmethod

# Define an abstract class `DataCleaner`
# This serves as a blueprint for different data cleaning techniques
class DataCleaner(ABC):
    
    # Define an abstract method `clean_data`
    # This method must be implemented by any subclass
    @abstractmethod
    def clean_data(self, data):
        pass  # No implementation in the abstract class

# Define a subclass `MissingValueCleaner` that inherits from `DataCleaner`
class MissingValueCleaner(DataCleaner):
    
    # Implement the `clean_data` method
    # This method prints a message for handling missing values
    def clean_data(self, data):
        print("Handling missing values")

# Create an instance of `MissingValueCleaner`
cleaner = MissingValueCleaner()

# Call the `clean_data` method for `MissingValueCleaner`
cleaner.clean_data("Dataset")  # Output: Handling missing values
