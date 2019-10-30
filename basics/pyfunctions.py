'''Functions in Python
DRY -> Don't repeat yourself
video-> https://youtu.be/9Os0o3wzS_I
'''

# Function declaration with pass statement
def fun():
    pass #-> if the fuction is simply declared but there is no functionality to it yet you can use the pass statement 

# Function call
print(fun()) # This'll print None

# Function declaration
def hello_func():
    print('This is a function!')

# Function call
hello_func()

# Function with return statement
def hello_func_ret():
    return 'Hello Batman!'

# Function call with Function chaining
print(hello_func_ret().upper())

# Function with Parameters
def func_param(greeting):
    return '{} Function.'.format(greeting)

print(func_param('Hi')) # if the argument value is not passed, 'func_param() missing 1 required positional argument: 'greeting'' error is displayed

# Function with Parameters. 'name' is a "Keyworded argument" and when no value is passed function will use the default value 'You'
def func_params(greeting, name='You'):
    return '{}, {}'.format(greeting, name)

# Function returns the string with default name value
print(func_params('Hey'))

# Function returns the string with passed name value
print(func_params('Hey', 'Batman'))

# *args-> variable length arguments, *kwargs->variable length Keyworded arguments
def student_info(*args, **kwargs):
    print(args) #This will return a tuple
    print(kwargs) #This will return a dictionary

# Passing values directly 
student_info('Math', 'art', name='Mani', age='27')

courses=['Math', 'art']
info = {'name': 'Mani', 'age': '27'}

''' If you pass the list and dict values as is, it'll return 'agrs->(['Math', 'art'], {'name': 'Mani', 'age': '27'}), and kwargs->{}' 
This is not desired. We need to unpack the list and dict and pass them as values like the above example. 
For that we should use *<listname> and **<dictname> i.e., *<args_name> to unpack args and **<kwargs_name> to unpack kwargs'''

student_info(courses, info)

student_info(*courses, **info)


# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Functions/snippets.txt
# Example:
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2020))

print(days_in_month(2017, 7))