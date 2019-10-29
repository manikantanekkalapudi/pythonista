'''First-Class Functions in Python
Source: https://en.wikipedia.org/wiki/First-class_function
In computer science, a programming language is said to have first-class functions if it treats functions as first-class citizens.
This means the language supports passing functions as arguments to other functions,
returning them as the values from other functions, and assigning them to variables or storing them in data structures.
'''

# Defining a square function
def square(x):
    return x * x

# Defining a cube function
def cube(x):
    return x * x * x

f = square(5) # Assigning a square() call with 5 to a variable f and now f holds the result of function call

print(square) # Prints '<function square at <location>>'
print(f)      # Prints result 25

f = square    # Here f and square point to the same function
print(f)
print(f(5))   # This returns 25

# Pass function as arguments-> Ex: map() take other functions as argument
# Custom map function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

# Call the Custom map function
squares = my_map(square, [1,2,3,4,5])
print(squares)

cubes = my_map(cube, [1,2,3,4,5])
print(cubes)

# Explaining Closure with First class functions
def logger(msg): # This is the first function which takes a msg parameter

    def log_message(): # This is a second function which is defined within the first function and takes no args, prints msg from first function
        print('log: ',msg)
    
    return log_message # Returning the second function as a result of first function call

log_hi = logger('Hi!') # Calling logger() with 'Hi!' as msg. This'll return a log_message() as the output
log_hi() # log_message() is obtained as the output from previous function call and after log_hi() it'll call the log_message() and that prints the msg we passed in

# Closure example.
# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/FC_Functions/fc_functions.py
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')