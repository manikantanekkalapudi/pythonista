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

# Initializing Employee class with the suitable input values for the constructor
emp1 = Employee('Manikantha', 'Nekkalapudi', 'mani@mycompany', 50000);
emp2 = Employee('Test', 'User', 'test.user@mycompany', 60000);
# Printing the class variable after instantiating
print(emp1.email)

# This is to print the full name and can be achieved using fullname() class method too 
print('{} {}'.format(emp1.first, emp1.last))

# Function call to get the full name of the employee
print(emp1.fullname())

# The following two lines will do the same
print(emp2.fullname())
# print(Employee.fullname(emp2)) #this is using class directly

# Call the apply_raise method
print(emp1.raise_amount) # or print(Employee.raise_amount)
# Print the updated pay
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

'''Source: https://code.tutsplus.com/tutorials/what-are-python-namespaces-and-why-are-they-needed--cms-28598
Namespace-> It is basically a system to make sure that all the names in a program are unique and can be used without any conflict.
There is a name-to-object mapping, with the names as keys and the objects as values'''
# Namespace for the class and the instance of the class
print(emp1.__dict__) #this instance doesn't have the raise_amount variable and it'll get it from the class
print(Employee.__dict__) # class has the raise_amount variable

# set the raise_amount using class
Employee.raise_amount = 1.05 #This will updated the raise_amount variable value for all the instances

# Set the raise_amount using the instance of the class
# This creates a 'raise_amount' variable within this particular instance emp1
# rest of the instances will have the raise_amount of the class 
emp1.raise_amount = 1.06
# the raise_amount is different for the class and emp1 instance
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
# here we can see the raise_amount is added to the emp1.__dict__
print(emp1.__dict__)

# print num_of_emps
print(Employee.num_of_emps)
