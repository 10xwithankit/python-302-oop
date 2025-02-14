# Define a class `Book`
class Book:
    
    # Define the constructor method (__init__)
    # This method initializes the book's attributes
    def __init__(self, title, author):
        
        # Assign the `title` parameter to the instance variable `self.title`
        self.title = title  
        
        # Assign the `author` parameter to the instance variable `self.author`
        self.author = author  

    # Define a special method `__str__`
    # This method returns a string representation of the book object
    def __str__(self):
        return f"'{self.title}' by {self.author}"

# Create an instance of the `Book` class
book = Book("Harry Potter", "J.K. Rowling")

# Print the book object
# This automatically calls the `__str__` method to return a formatted string
print(book)  # Output: 'Harry Potter' by J.K. Rowling
