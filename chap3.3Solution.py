# Assign a string value to the variable `x`
x = "Python"

# Assign `x` to another variable `y`
# `y` now refers to the same object as `x`
y = x  

# Check if `x` and `y` reference the same object in memory
print(id(x) == id(y))  # Output: True, both reference the same object

# Assign a new string value to `y`
# This creates a new object and `y` now refers to a different memory location
y = "Java"

# Check again if `x` and `y` reference the same object in memory
print(id(x) == id(y))  # Output: False, they now point to different objects
