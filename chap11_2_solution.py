# Define a class `Employee`
class Employee:
    
    # Define the constructor method (__init__)
    # This method initializes the employee's name and position
    def __init__(self, name, position):
        self.name = name  # Assign the employee's name
        self.position = position  # Assign the employee's position
    
    # Define a method `work`
    # This method prints a message indicating the employee is working
    def work(self):
        print(f"{self.name} is working as a {self.position}.")

# Define a class `Company`
class Company:
    
    # Define the constructor method (__init__)
    # This method initializes the company's name and maintains a list of employees
    def __init__(self, company_name):
        self.company_name = company_name  # Assign the company name
        self.employees = []  # Composition: A company has employees
    
    # Define a method `add_employee`
    # This method adds an employee to the company's list
    def add_employee(self, employee):
        self.employees.append(employee)
    
    # Define a method `show_employees`
    # This method prints the company's employees and their roles
    def show_employees(self):
        print(f"Employees at {self.company_name}:")
        for emp in self.employees:
            emp.work()  # Call the `work` method for each employee

# Create instances of `Employee`
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Designer")

# Create an instance of `Company`
company = Company("TechCorp")

# Add employees to the company
company.add_employee(emp1)
company.add_employee(emp2)

# Display the employees working at the company
company.show_employees()
