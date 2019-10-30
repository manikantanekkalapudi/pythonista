'''
video-> https://youtu.be/CqvZ3vGoGs0
'''

# importing my_module
import my_module # From this statement we're able to access all the functions, variables and etc. in the file

# from my_module import find_index # This will only access to the find_index() in the my_module and nothing else

# List of courses
courses = ['Math', 'Art', 'Physics', 'CompSci']

# Calling the find_index() in my_module by passing list and key value to get the index of the key value in the list
index = my_module.find_index(courses, 'Art')
print(index)

import sys
print(sys.path) # This will print all the modules python will look for when importing something