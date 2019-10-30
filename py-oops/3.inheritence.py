'''
Inheritence in Python
video-> https://youtu.be/RSl87lqOXDE

Source: https://www.javatpoint.com/inheritance-in-python
Inheritance is an important aspect of the object-oriented paradigm. Inheritance provides code reusability to the program because we can use an existing class to create a new class instead of creating it from scratch.
In inheritance, the child class acquires the properties and can access all the data members and functions defined in the parent class. A child class can also provide its specific implementation to the functions of the parent class.
'''
class Employee:

    # Class variables
    num_of_emps = 0 # Variable to count the no. of employees
    raise_amount = 1.04

    # '''__init__ is the constructor for the class and 
    # all the variables that the class takes can be initialized here
    def __init__(self, first, last, pay):
        # Instance variables initialized in the constructor
        self.first = first
        self.last = last
        self.email = first +'.'+ last +'@company.com'
        self.pay = pay
        
        # This variable doesn't need to 'self' as it belongs to the class and not any particular instance
        Employee.num_of_emps += 1

    '''Class method-> They'll have self as the first param
    If we forget 'self' parameter for method param it'll throw the following error:
    "<method_name> takes 0 positional arguments but 1 was given" error-> it's confusing message!'''
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Class method to apply the raise   
    def apply_raise(self):
        #We can also use 'Employee.raise_amount' or 'self.raise_amount' but never only 'raise_amount'
        self.pay = self.pay * self.raise_amount 
    
    # This is using the decorators to declare classmethod
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


    # Class methods as alternative constructors -> use these classmethods in order to provide multiple ways of creating objects
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # Employee is nothing but cls
        return cls(first, last, pay)

    '''Source: https://www.journaldev.com/18722/python-static-method
    Static method -> Static methods in Python are extremely similar to python class level methods, the difference being that a static method is bound to a class rather than the objects for that class.
    This means that a static method can be called without an object for that class. This also means that static methods cannot modify the state of an object as they are not bound to it. Let’s see how we can create static methods in Python.
    
    Static method -> It has a logical connection to the class but doesn't depend on any specific instance of the class or class variable'''
    @staticmethod
    def is_workday(day):  #doesn't take an instance or a class as the first argument and we can pass any argument
        if (day.weekday() == 5) or (day.weekday()) == 6:
            return False
        else:
            return True


# This is the Developer class trying to inherit Employee class
class Developer(Employee):
    # This is for the Developer class raise
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # This is preferred for single inheritence
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        # This is preferred for multiple inheritence
        # Employee.__init__(self,first, last, pay)

class Manager(Employee):
    # initializing Manager class after inheriting the Employee class
    def __init__(self, first, last, pay, employees=None):
        # Using Employee class constructor to instantiate the Manager class constructor
        super().__init__(first, last, pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees
    
    # Add an employee under a manager
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # Remove an employee under a manager
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.append(emp)
    
    # Print all employees under an employee
    def print_employees(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# Instantiating Employee class with all the required values for the constructor variables
# dev1 = Employee('Manikantha', 'Nekkalapudi', 50000); -> This'll have 1.04 as raise_amount even after the inheritence change
# dev1.apply_raise() -> It's seen here

# Instantiating Developer class with all the required values for the constructor variables
dev1 = Developer('Manikantha', 'Nekkalapudi', 50000, 'java')
dev2 = Developer('Test', 'User', 60000, 'python')

# The below line will print MRO, objects, variables inherited and all the details of the Developer class
# print(help(Developer))

# Print dev1's email
print(dev1.email)

# Print dev1's prog_lang
print(dev1.prog_lang)

# Current dev pay raise
print(dev1.pay)

# Apply raise for dev1
dev1.apply_raise()

# print dev1's updated pay
print(dev1.pay)

# Initilize manager1 object of Manager type and add list of employees([dev1]) to the same
manager1 = Manager('Sue', 'Smith', 90000, [dev1])
print(manager1.email)

# Print all the employees manager1 object
manager1.print_employees()

# Add dev2 the employee from manager1 object
manager1.add_employee(dev2)

# Print all the employees manager1 object
manager1.print_employees()

# Remove dev1 the employee from manager1 object
manager1.remove_employee(dev1)

# Print all the employees manager1 object has finally
manager1.print_employees()

# Checking if an manager1 object is of Manager class-> True 
print(isinstance(manager1, Manager))

# Checking if an manager1 object is of Developer class-> False
# Here first param is the object checked against the second value which is a class
print(isinstance(manager1, Developer))

# Checking if Manager is a subclass of Employee-> True
# Here the first param is the one to be checked to be a subclass against second param
print(issubclass(Manager, Employee))
