'''
Source: https://dbader.org/blog/python-dunder-methods
Special methods or Magic methods or Dunder Methods:
    Dunder methods let you emulate the behavior of built-in types. 
    For example, to get the length of a string you can call len('string').
    But an empty class definition doesn’t support this behavior out of the box.
    We need to define the functionality.
'''
# Employee class to replicate the Employee Management System 
class Employee:

    # Class variables
    num_of_emps = 0 # variable to count the no. of instantiations of Employee class (which is no. of employees)
    raise_amount = 1.04

    '''__init__ is the constructor for the class and 
    all the variables that the class takes can be initialized here'''
    def __init__(self, first, last, email, pay):
        # instance variables initialized in the constructor
        self.first = first;
        self.last = last;
        self.email = email;
        self.pay = pay;
        
        # This variable doesn't need to have 'self' as it belongs to the class and not any particular instance
        Employee.num_of_emps += 1

    '''Class method-> They'll have self as the first param
    If we forget 'self' parameter for method param it'll throw the following error:
    "<method_name> takes 0 positional arguments but 1 was given" error-> it's confusing message!'''
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Class method to apply the raise   
    def apply_raise(self):
        #we can also use 'Employee.raise_amount' or 'self.raise_amount' but never only 'raise_amount'
        # because it is a class variable
        self.pay = self.pay * self.raise_amount
    
    # An unambiguous representation of the object and should used for debugging and logging.
    # It's meant to be seen by other developers
    # It's minimum to have this method because __str__ method call will fallback to __repr__ if not implemented
    def __repr__(self):
        return "Employee('{}' , '{}', '{}')".format(self.first, self.last, self.email, self.pay)

    # Readable representation of the object and it is meant be a display to the end users
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)
    
    # Dunder method to add the pay of two employees
    def __add__(self, other):
        return self.pay + other.pay
    
    # Dunder method to find length of employee full name
    def __len__(self):
        return len(self.fullname()) 
    
# Initializing Employee class with the suitable input values for the constructor
emp1 = Employee('Manikantha', 'Nekkalapudi', 'mani@mycompany', 50000);
emp2 = Employee('Test', 'User', 'test.user@mycompany', 60000);

# This line will print the string defined in the __repr__ method displayed above
print(repr(emp1))
# This line will print the string defined in the __str__ method displayed above
print(str(emp1))

# This line will print the string defined in the __repr__ method displayed above
print(emp1.__repr__())
# This line will print the string defined in the __str__ method displayed above
print(emp1.__str__())

# Print statement uses dunder method 
# int __add__ method-> adds the numbers 
print(int.__add__(1,2))

# str __add__ method-> concats the chars
print(str.__add__('a', 'b'))

# Printing the __add__ method's result that is declared above
print(emp1+emp2)

# len() of a string. The following statements will print the same method
print(len('abcd'))
print('abcd'.__len__())

# Calling __len__ method defined above
print(len(emp1.fullname()))

