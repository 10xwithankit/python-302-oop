# Import the ABC module to define an abstract class
from abc import ABC, abstractmethod

# Define an abstract class `DataSource`
# This serves as a blueprint for different data sources
class DataSource(ABC):
    
    # Define an abstract method `read_data`
    # This method must be implemented by any subclass
    @abstractmethod
    def read_data(self):
        pass  # No implementation in the abstract class

# Define a subclass `CSVSource` that inherits from `DataSource`
class CSVSource(DataSource):
    
    # Implement the `read_data` method
    # This method prints a message for reading data from a CSV file
    def read_data(self):
        print("Reading data from CSV file")

# Define another subclass `SQLSource` that inherits from `DataSource`
class SQLSource(DataSource):
    
    # Implement the `read_data` method
    # This method prints a message for reading data from an SQL database
    def read_data(self):
        print("Reading data from SQL database")

# Create an instance of `CSVSource`
csv = CSVSource()

# Call the `read_data` method for `CSVSource`
csv.read_data()  # Output: Reading data from CSV file
