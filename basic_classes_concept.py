# Define a class named 'Employee'
class Employee:
    # Class variable to define a raise amount for all employees
    raise_amount = 1.04
    # Class variable to keep track of the number of employees
    num_of_emps = 0

    # Constructor method to initialize instances of the class
    def __init__(self, first, last, pay):
        # Instance variables for first name, last name, and pay
        self.first = first
        self.last = last
        self.pay = pay
        # Instance variable to generate the email based on first and last name
        self.email = f'{first.lower()}.{last.lower()}@company.com'
        # Increment the number of employees when a new employee is created
        Employee.num_of_emps += 1

    # Method to return the full name of the employee
    def fullname(self):
        # Concatenate the first and last name to create the full name
        self.fullname = f'{self.first} {self.last}'
        return self.fullname

    # Method to apply a raise to the employee's pay
    def apply_raise(self):
        # Multiply the current pay by the raise amount and convert to an integer
        self.pay = int(self.pay * self.raise_amount)

    # Class method to create an employee from a string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static method to check if a given day is a work day
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2024, 1, 26)
# Check if the given date is a work day
print(Employee.is_work_day(my_date))

emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-50000'

# Create instances of the Employee class from string representations
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)

new_emp_2 = Employee.from_string(emp_str_2)
print(new_emp_2.email)
print(new_emp_2.pay)

new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email)
print(new_emp_3.pay)

# Create instances of the Employee class
emp_1 = Employee('ahsan', 'ilahi', 50000)
emp_2 = Employee('abdul', 'rehman', 60000)
emp_3 = Employee('rabia', 'majeed', 70000)

# Print information for the first employee
print(emp_1.fullname())
print(emp_1.pay)
print(emp_1.email)

print('\n')

# Print information for the second employee
print(emp_2.fullname())
print(emp_2.pay)
print(emp_2.email)

print('\n')

# Print information for the third employee
print(emp_3.fullname())
print(emp_3.pay)
print(emp_3.email)

# Print the total number of employees using the class variable
print(Employee.num_of_emps)
