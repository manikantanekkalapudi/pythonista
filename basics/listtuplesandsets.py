'''Lists, Tuples and Sets in Python
List-> Hetrogenous collection of items which are both ordered and mutable
Tuple-> Hetrogenous collection of items which are ordered and NOT mutable
Set-> Hetrogenous collection of items which are neither ordered nor mutable
'''

# Declaring a list of string values
courses = ['History', 'Math', 'Physics', 'CompSci']

# Printing the list
print(courses)

# Length of the list or # items in the list
print(len(courses))

# Indexing in list-> indexes start from 0 till length-1 for +ve indices. For -ve indices,
# they start with -1 for the last item and till the -length for the first item in the list
print(courses[3])

# First Element of the list
print(courses[0]) # or print(courses[-4])

# Last item
print(courses[3]) # or print(courses[-1])

# For non-existent index like 4 in this case it'll throw 'list index out of range' error
# print(courses[4])

# Slicing and Dicing in list
print(courses[:2]) # or print(courses[0:2])
print(courses[2:]) # This will print the values from 2 till the end of the list

# Append-> Adding an item at the end of the list
courses.append('Art')
print(courses)

# Insert-> Adding an element at a specific index. First param is location/index and second is item to be inserted
courses.insert(0, 'Commerce')
print(courses)

# Extend-> Adding a list of values from a list to another list. 
# This will add all the elements of the second list at the end of first list
course = ['Humanities', 'Geology']
courses.extend(course)
print(courses)

# If a list is inserted at 0 in other list, then the whole list will be inserted as list at 0
courses.insert(0, course)
print(courses)
print(courses[0])

# Remove values from the list
courses.remove('Commerce') # If item not found, 'ValueError: list.remove(x): x not in list' error will be displayed
print(courses)

# Pop-> works like pop() in stack or queue and removes the last element in the list
removed = courses.pop()
print(removed)

# Reverse a list
courses.reverse()
print(courses)

# Removing list within the list
courses.pop()
print(courses)

# Sort a list
courses.sort() # All the elements should be of same type else it'll throw error
print(courses)

# Number list example
nums = [3,5,2,6,1]
nums.sort()
print(nums)

# Sort in reverse/decending order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# Sorted()->Obtain the sorted list without altering the original list
sorted_courses = sorted(courses)
print(sorted_courses)

# Min, Max
print(min(nums)) #Similarly for max -> max(), sum->sum()

# Index of a certain value
print(courses.index('CompSci')) # It'll return the index of first occurence of the element from the 0th index
# If the element is not in the list-> '<element> is not in list' error is displayed

# Check if the values is present in the list
print('Art' in courses) # returns True or False

# Print all the elements in the list
for course in courses:
    print(course)

# Access both the index and value using Enumerate()
for index, course in enumerate(courses, start=1): #start determines from which value the index starts
    print(index, course)

# All the list items as a comma seperated values in a string
courses_str = ', '.join(courses)
print(courses_str)

# Split a string into a list
new_list = courses_str.split(', ')
print(new_list)

# Additional properties of a list
courses2 =courses
print(courses2)

courses[0] = 'Biology'
print(courses2) # Here courses2[0] value is changed when we changed courses[0] to 'Biology' because both the variables are pointing to only one memory/object

# Tuple declaration
tup = ('Physics', 'Math', 'Humanities', 'History', 'CompSci', 'Art')

# Indexing in tuple
print(tup[0]) # This works same as the list

# Modifying elements in a tuple
# tup[0] = 'Commerce' #This will throw 'TypeError: 'tuple' object does not support item assignment' error

# Set declaration
course_set = {'Biology', 'Math', 'Humanities', 'History', 'CompSci', 'Art'}
print(course_set) # The above order of elements in the set is not maintained because Set doesn't have an order

# Memebership test for an element in a Set
print('Math' in course_set) #Sets are optimised to do this i.e., search for an element better than lists/tuples

# Set operations
art_courses = {'History', 'Art', 'Math', 'Design'}

# Intersection
print(course_set.intersection(art_courses))

# Difference
print(course_set.difference(art_courses)) #Only the course in course_set that are not common will be displayed

# Union
print(course_set.union(art_courses))

# Empty list, tuple, set
lst = [] # or lst = list()

tupl = ()

sett = {} # This'll create an empty dict not empty set
print(type(sett))
sett = set()
print(type(sett)) # This'll create an empty set