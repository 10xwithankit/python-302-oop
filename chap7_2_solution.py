# Define a class `Book`
class Book:
    
    # Define the constructor method (__init__)
    # This method initializes the book's attributes
    def __init__(self, title, author):
        
        # Assign the `title` parameter to the instance variable `self.title`
        self.title = title  
        
        # Assign the `author` parameter to the instance variable `self.author`
        self.author = author  

    # Define a special method `__repr__`
    # This method returns an official string representation of the book object
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"

# Create an instance of the `Book` class
book = Book("Harry Potter", "J.K. Rowling")

# Print the official string representation of the book object using `repr()`
print(repr(book))  # Output: Book(title='Harry Potter', author='J.K. Rowling')
