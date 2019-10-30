'''
Property Decorators- Getters, Setters and Deleters in Python
video-> https://youtu.be/jCzT9XFZ5bw
'''

class Employee:

    # '''__init__ is the constructor for the class and 
    # all the variables that the class takes can be initialized here
    def __init__(self, first, last):
        # Instance variables initialized in the constructor
        self.first = first
        self.last = last
        # self.email = first +'.'+ last +'@company.com'
    
    # Method call is the not the right way because we've to change every single instance of the email attibute
    # to this function call. Now, adding @property will above the method will not change anything.
    # i.e., we can access email or any function as an attribute 
    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)
    
    # Getter attribute for full name
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    # Defining the setter for full name
    @fullname.setter
    def fullname(self, name):
        first, last = name.split()
        self.first = first
        self.last = last
    
    # Defining the deleter for full name 
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

# Instantiating Employee object
emp_1 = Employee('John', 'Smith')

# Updating the first name is updated to Jim
emp_1.first = 'Jim'

# Setter for full name
emp_1.fullname = 'Manikantha Nekkalapudi' # This will initially throw error when there is no setter method to accept a full name

# Printing first name
print(emp_1.first)

# Printing the Employee email-> Email still has old first name 
# when the email is an class variable. If it has a property decorator 
# then the email will be updated with latest first name 
print(emp_1.email)

# Printing full name->The first name is the latest one here
# print(emp_1.fullname()) #This will be used when it's a class function
# The below line is a getter method to delete the full name of an employee
print(emp_1.fullname)

# Deleter for full name
del emp_1.fullname