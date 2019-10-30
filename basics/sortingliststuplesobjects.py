'''Sorting Lists, Tuples, Dict and Objects in Python
video-> https://youtu.be/D3JvDWO-BY4
'''

# Declaring a list
lst = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# Sorting a list using sorted() -> This will return a list and we need to store in a different variable
sorted_lst = sorted(lst)
print(sorted_lst)

# Sorting a list using sort() -> This will not return a new list but the original list is sorted
lst.sort()
print(lst)

# Sort in descending order
lst.sort(reverse=True)
print(lst)

# Why choose sorted() over sort()? -> sort() works on list specifically and sorted() works on any iterable
# Example-> Tuple doesn't have sort() and sorted() can be used there. Sorted can't be used for Set because it doesn't have an inherent order
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
# tup.sort() -> This'll throw ''tuple' object has no attribute 'sort'' error
sorted_tup = sorted(tup)
print(sorted_tup) #This return a List!

# sorted() on dict
dic = {'name':'mani', 'job':'programming', 'age':27, 'os':'Linux'}
sorted_dic = sorted(dic)
print(sorted_dic) # This'll return a sorted list of keys

# Sort the absolute value
lst = [-6,-5,-4,1,2,3]
sorted_lst = sorted(lst)
print(sorted_lst) #Prints the same list as the above one

# Sort the absolute value
sorted_lst = sorted(lst, key=abs) #key=abs will map all the values in list to abs() and then sorts it
print(sorted_lst)

# Sorting objects using sorted()
class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

# Object declaration for Employee class
e1 = Employee('Mani', 27, 50000)
e2 = Employee('Sarah', 33, 55000)
e3 = Employee('John', 45, 70000)

# List of employees
employees = [e1, e2, e3]

# Custom sort function for sorting objects
def e_sort(emp):
    # return emp.name #return employee name to sort employees according to name
    return emp.age #return employee age to sort employees according to age
    # return emp.salary #return employee salary to sort employees according to salary

# Sort using sorted() and key with custom sort function
sorted_emp = sorted(employees, key = e_sort, reverse = True)
print(sorted_emp)

# Sort using kay and lambda function
sorted_emp = sorted(employees, key=lambda e: e.name)
print(sorted_emp)

# Using attrgetter instead of custom e_sort(). Both does the same work.
from operator import attrgetter

sorted_emp = sorted(employees, key = attrgetter('salary'), reverse = True)
print(sorted_emp)