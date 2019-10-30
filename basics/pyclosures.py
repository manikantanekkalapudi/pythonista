'''Closures in Python- How to Use Them and Why They Are Useful
video-> https://youtu.be/swU3c34d2NQ

Pre-requisite: Know about First class functions from firstclassfunction.py
'''

# Defining a closure function which returns the result of inner function call
def outer_func1():
    message = 'Hi'

    def inner_func1():
        print(message)

    return inner_func1()

outer_func1()

# Defining a closure function which returns the inner function
def outer_func2():
    message = 'Hi'

    def inner_func2():
        print(message)

    return inner_func2

my_func = outer_func2()
print(my_func.__name__)
my_func() #<- This is a closure which is an inner function and remembers and has access to variables in local scope in which it was created even after the outer function has finished executing
my_func()

# Defining a closure function which takes msg parameter and returns the inner function
def outer_func3(msg):
    message = msg

    def inner_func3():
        print(message)

    return inner_func3

hi_func = outer_func3('Hi')
hello_func = outer_func3('Hello')

# The below functions(inner) remembers the message
hi_func()
hello_func()

'''
Note: A closure closes over the free variables from their environment and in the above case 'message' is the variable
'''

# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Closures/closure.py

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

# This function takes a function 'func' as a parameter
def logger(func):
    # This function takes any number of arguments
    def log_func(*args):
        # Logging that the function 'func' will run with the arguments passed
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__, args))
        # Call 'func' with arguments and print the result
        print(func(*args))
    
    # Returning inner log function
    return log_func

# Add funtion -> It'll be passed to outer function above
def add(x, y):
    return x+y

# Subtract function -> It'll be passed to outer function above
def sub(x, y):
    return x-y

# Calling the outer function by passing 'add' and 'sub' function
add_logger = logger(add)
sub_logger = logger(sub)

# Calling the inner function for 'add' function by passing the arguments
add_logger(3, 3)
add_logger(4, 5)

# Calling the inner function for 'sub' function by passing the arguments
sub_logger(10, 5)
sub_logger(20, 10)

# This will generate an 'example.log' file in the cwd with the info mentioned in the inner function above
