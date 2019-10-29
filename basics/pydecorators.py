'''Decorators in Python - Dynamically Alter The Functionality Of Your Functions
Pre-requisite: 
1. Know about First class functions from firstclassfunction.py
2. Know about Closures from pyclosures.py

First class functions-> They allow us to treat functions like any other object. 
We can pass functions as argument to other function, 
we can return function and assign functions to a variables.

Closure-> Allows us to take advantage of First class functions and return an inner function 
that remembers and has access to variables local to the scope in which they we're created.
'''

'''
What are Decorators?
A) A decorator is a function that takes another function as an argument, 
adds some kind of functionality and then returns another function. 
All of this without changing the source code of the original function
'''

from functools import wraps

# Decorator declaration
# This is the Decorator function which takes a function as an input argument
def decorator_function(original_function):
    # This is a Wrapper function which returns the result of 'original_function' passed to 'decorator_function'
    # Add '*args, **kwargs' to the function parameters so that the below function can run with any kinds of parameters
    def wrapper_function(*args, **kwargs):
        # Any functionality can be added and the following line is added after the creation of the decorator
        print('Wrapper executed this before {}'.format(original_function.__name__))
        
        # Add '*args, **kwargs' to the function parameters below too
        return original_function(*args, **kwargs)
    # Return the Wrapper function
    return wrapper_function

# This is the Original function to be passed in decorator function
def display1():
    print('display function ran')

# This will call the 'decorator_function' with the 'display' as argument and return wrapper function 
decorated_display = decorator_function(display1)

# From the above step 'decorated_display' holds the 'wrapper_function'. 
# Below is the call for 'wrapper_function' and it calls the 'display' function that we passed to 'decorator_function'
decorated_display()

'''
@decorator_function above display function is equal to -> display = decorator_function(display)
'''
@decorator_function
def display():
    print('display function ran')

display()

# Decorator does work with the functions that takes arguments unless we 
@decorator_function
def display_info1(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info1('Mani', 22) # This will throw 'TypeError: wrapper_function() takes 0 positional arguments but 2 were given' when the wrapper_function will not accept any parameters


''' Classes as Decorators'''
class decorator_class(object):
    # Pass the original_function to the __init__ method similar to passing original_function to decorator_function
    def __init__(self, original_function):
        self.original_function = original_function
    
    # Adding the functionality to the original function using __call__(). This will behave same as the wrapper_fuction() above
    def __call__(self, *args, **kwargs):
        # Any functionality can be added and the following line is added after the creation of the decorator
        print('__call__ executed this before {}'.format(self.original_function.__name__))
        
        # Add '*args, **kwargs' to the function parameters below too
        return self.original_function(*args, **kwargs)

@decorator_class
def display_info1(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info1('Mani', 22)

'''Practical examples for Decorators'''
# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Decorators/snippets.txt
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)
    
    # Wrapping the my_logger_wrapper with the orig_func to avoid returning the wrapper and return orig_func
    @wraps(orig_func)
    def my_logger_wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return my_logger_wrapper

@my_logger
def display_info2(name, age):
    print('display_info2 ran with arguments ({}, {})'.format(name, age))

display_info2('Mani', 22)

def my_timer(orig_func):
    import time

    # Wrapping the my_logger_wrapper with the orig_func to avoid returning the wrapper and return orig_func
    @wraps(orig_func)
    def my_timer_wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return my_timer_wrapper

import time

@my_timer
def display_info3(name, age):
    time.sleep(1)
    print('display_info3 ran with arguments ({}, {})'.format(name, age))

display_info3('Mani', 22)

# Using multiple decorators for one function
@my_timer
@my_logger
def display_info4(name, age):
    time.sleep(1)
    print('display_info4 ran with arguments ({}, {})'.format(name, age))

display_info4('Tom', 22)

'''
@my_logger
@my_timer

The above one is equivalent to display_info4 = my_logger(my_timer(display_info4))
This will return this result-> 'display_info4 ran with arguments (Mani, 22), my_logger_wrapper ran in: 1.0010871887207031 sec'
Which is not correct because we wanted to display 'display_info4 ran in: 1.0010871887207031 sec'

It doesn't have any effect even if we change the order of the decorators.

What was happening here is when we cascade the decorators 'wrapper' function is returned after the first decorator call and not the original function.

How to fix this?
We can fix using functools module and wraps decorator. Importing the same at the beginning

After this we'll get the result that we need after stacking the decorators

'''

