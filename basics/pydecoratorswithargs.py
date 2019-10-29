'''Decorators With Arguments in Python'''

# Prefix to the decorator
def prefix_decorator(prefix_message):
    # Decorator declaration
    # This is the Decorator function which takes a function as an input argument
    def decorator_function(original_function):
        # This is a Wrapper function which returns the result of 'original_function' passed to 'decorator_function'
        # Add '*args, **kwargs' to the function parameters so that the below function can run with any kinds of parameters
        def wrapper_function(*args, **kwargs):
            # Any functionality can be added and the following line is added after the creation of the decorator
            print(prefix_message, 'Executed before {}'.format(original_function.__name__))
            
            result = original_function(*args, **kwargs)

            print(prefix_message, 'Executed after ',original_function.__name__, '\n')

            return result

        # Return the Wrapper function
        return wrapper_function
    
    # Return Decorator function
    return decorator_function

# Declaring a function with the @decorator_function annotation
@prefix_decorator('Testing-')
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Mani', '23')
display_info('John', '23')