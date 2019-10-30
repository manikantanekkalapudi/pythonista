'''Conditional Statements and Booleans - If, Else, and Elif Statements
video-> https://youtu.be/DZwmZ8Usvnk
'''

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is

'''
# False Values-> These values evaluvates to False in the condition:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.


condition = False

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

'''

# if statement
# lang = 'Python'
lang = 'Java'

if lang == 'Python':
    print('Language is Python!')

elif lang == 'Java':
    print('Language is Java!')
else:
    print('No Match')

'''Note:
        Python doesn't have a Switch case'''

# Boolean operations-> and, or & not
# and-> both should be True to enter if block
user = 'Admin'
logged_in = False

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

# or-> any one can be True to enter if block
user = 'Admin'
logged_in = True

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Credentials')

# not-> negates the values
user = 'Admin'
logged_in = False
if not logged_in:
    print('Please login!')
else:
    print('Welcome')


# Source: http://www.blog.pythonlibrary.org/2017/02/28/python-101-equality-vs-identity/
# Object Identity:  is ->
num = 1
num_two = num
print(num == num_two) # It print True

# Here both num and num_two are pointing to the same address
print(id(num))
print(id(num_two))

# When you ask Python the question “list_one is list_two”, you receive False because they're at different locations in the memory
list_one = [1, 2, 3]
list_two = [1, 2, 3]
print(list_one is not list_two)

# This returns True because all the elements in list_one are same as list_two
print(list_one == list_two)

# When you create two variables that point to the same object any modification to the objects will reflect under both variable names
list_one = list_two = [1, 2, 3]
print(list_one == list_two)
print(list_one is list_two) # This will print True because list_one and list_two are pointing to the same location
list_two.append(5)
print(list_one)

'''
Note:
Equality is basically just asking if the contents of the two object are the same 
and in the case of lists, it needs to be in the same order as well. 
Identity in Python refers to the object you are referring to. 
In Python, the identity of an object is a unique, constant integer (or long integer) 
that exists for the length of the object’s life.

'''
