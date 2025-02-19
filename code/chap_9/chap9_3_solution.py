# Import the ABC module to define an abstract class
from abc import ABC, abstractmethod

# Define an abstract class `DataSource`
# Abstract classes cannot be instantiated and must be inherited by subclasses
class DataSource(ABC):
    
    # Define an abstract method `read_data`
    # This method must be implemented by any subclass
    @abstractmethod
    def read_data(self):
        pass

# Define a subclass `CSVSource` that inherits from `DataSource`
class CSVSource(DataSource):
    
    # Implement the `read_data` method
    # This method prints a message indicating data is being read from a CSV file
    def read_data(self):
        print("Reading data from CSV file")  # Output will now be printed

# Define another subclass `SQLSource` that inherits from `DataSource`
class SQLSource(DataSource):
    
    # Implement the `read_data` method
    # This method prints a message indicating data is being read from an SQL database
    def read_data(self):
        print("Reading data from SQL database")  # Output will now be printed

# Create instances of `CSVSource` and `SQLSource`
csv = CSVSource()
sql = SQLSource()

# Call the `read_data` method for `CSVSource` and `SQLSource`
csv.read_data()  # Output: Reading data from CSV file
sql.read_data()  # Output: Reading data from SQL database
