'''F-Strings - How to Use Them and Advanced String Formatting in Python'''
# F-Strings -> py >= v3.6

# Creating a normal string using string formatting
first_name = 'manikantha'
last_name = 'nekkalapudi'

sentence = 'My name is {} {}'.format(first_name, last_name)
print(sentence)

# To represent this as an fstring we'll add 'f' at the beginning of the string. We can run functions within the placeholders in a string
sentence = f'My name is {first_name.capitalize()} {last_name.capitalize()}' # This is very intiitive and reduces going back and forth
print(sentence)

# Accessing dict values within the string. Use "" to avoid syntax errors.
person = {'name': 'Mani', 'age': 27}
sentence = f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)

# Calculations withing fstring
sentence = f"4 times 11 is {4 * 11}"
print(sentence)

# fstring in loop
for i in range(1, 5):
    sentence = f'The number is {i:02}'
    print(sentence)

# fstring with floating point number formatting
pi = 3.14159265
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

# fstring with Datetime formatting
from datetime import datetime
birthday = datetime(1990, 1, 1)
sentence = f'Jenn has birthday on {birthday:%B %d, %Y}'
print(sentence)