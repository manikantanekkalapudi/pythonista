'''Strings in Python'''

# Variable holding a simple string value
message = 'Hello world!'

# Printing the string variable
print(message)

# String value with a ' -> This needs an escape character to ignore the additional ' in the string
# or we can use "" when the string has ' and viceversa. It is a best practice to have an escape character
message = 'Mani\'s pen'

print(message)

# Multi-line string

message = '''I'm Ironman!
                        -Tony Stark'''

print(message)

# Length of the string
print(len(message))

# Indexing in string-> indexing starts from 0 at the first char in the String
print(message[4])

# Slicing and Dicing of the string-> first value of the slice(0) is inclusive and the last value is exluded. 
# i.e., only till 0 to 5 values are considered. [:6]->This starts from 0th index. [6:]-> starts from 6 till the end of string
print(message[0:6])

# String in lower case
print(message.lower()) # Similarly for uppercase -> .uppercase()

# Count # occurances of char in a string
print(message.count('I'))

# Find a char/substring in a string
print(message.find('Ironman')) #This prints the starting/lower index of occurance of Ironman. i.e., 4. If not found, -1 will be returned

# Replacing a substring in a string. Here 'message.replace' will return a new string and it should be stored in a new string
new_message = message.replace('''I'm Ironman!
                        -Tony Stark''', 'I\'m Batman!')

print(new_message)

# String concatination
greeting = 'Hello'
name = 'Mani'

message = greeting +' '+name+'. Welcome!'

# Formatted strings
message = '{} {}. Welcome!'.format(greeting, name)

print(message)

# fstrings -> >=v3.6
message = f'{greeting} {name.upper()}. Welcome!'
print(message)

# dir() will give all the attributes and methods for that variable. Here we're passing a string
print(dir(message))
'''
O/p for a string variable:
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
'__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
'__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 
'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 
'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 
'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'''

# Info about a class-> Displays all the information about the string class
print(help(str))

