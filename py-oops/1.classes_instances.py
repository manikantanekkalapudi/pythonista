# Employee class to replicate the EMS 
class Employee:

    # class variables
    num_of_emps = 0 # variable to count the no. of employees
    raise_amount = 1.04

    # '''__init__ is the constructor for the class and 
    # all the variables that the class takes can be initialized here
    def __init__(self, first, last, email, pay):
        # instance variables initialized in the constructor
        self.first = first;
        self.last = last;
        self.email = email;
        self.pay = pay;
        
        # This variable doesn't need to 'self' as it belongs to the class and not any particular instance
        Employee.num_of_emps += 1

    # class method
    # if we forget 'self' parameter for methods it'll throw 
    # "<method_name> takes 0 positional arguments but 1 was given" error-> it's confusing
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # class method to apply the raise   
    def apply_raise(self):
        #we can also use 'Employee.raise_amount' or 'self.raise_amount' but never only 'raise_amount'
        self.pay = self.pay * self.raise_amount 

# Instance of the class initialized with all the necessary class variables
emp1 = Employee('Manikantha', 'Nekkalapudi', 'mani@mycompany', 50000);
emp2 = Employee('Test', 'User', 'test.user@mycompany', 60000);
# printing the class variable after instantiating
print(emp1.email)

# This is to print the full name and can be achieved using method too 
print('{} {}'.format(emp1.first, emp1.last))

# function call to get the full name
print(emp1.fullname())

# The following two lines will do the same
print(emp2.fullname())
# print(Employee.fullname(emp2)) #this is using class directly

# call the apply_raise method
print(emp1.raise_amount) # or print(Employee.raise_amount)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)

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
