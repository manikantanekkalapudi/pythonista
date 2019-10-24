'''Dictionaries or Key-Value pairs'''

# Dict declaration
student={'name':'John', 'age':24, 'courses':['Math','CompSci']}

# Accessing the values from the dictionary using keys
print(student['name'])

# Accessing the key that is not in the dict
# print(student['phone_number']) ->This will throw 'KeyError:<keyname>' error

# get() to access the elements
print(student.get('age'))

# Accessing an non-existent element using the get(). Second arg is the custom message when the key is not found
print(student.get('phone_number', 'Not Found'))

# Adding an key-value pair to the dictionary
student['phone_number'] = 5555555555 # If the key is already present then the value will be updated

# Here name is updated
student['name'] = 'Jane'
print(student)

# Update using update() -> This can update multiple values at once
student.update({'name': 'Bruce', 'age':26, 'phone_number': 2313121312})
print(student)

# Delete a key using del
# del student['age']

# Delete a key using pop()
age = student.pop('age')
print(age)

# Length of dict
print(len(student))

# Keys in a dict
print(student.keys())

# Values in a dict
print(student.values())

# Keys and values in a dict
print(student.items())

# Loop through all the elements(keys and values) in a dict
for key, value in student.items():
    print(key, value)
