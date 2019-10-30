'''String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates in Python
Video-> https://youtu.be/vTX3IwquFkc
'''

# Declaring a dict
person_dict = {'name': 'Jenn', 'age': 23}

# Concatinating a string-> This is not a very good approach and very error prone at times
# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)

sentence = 'My name is {} and I am {} years old.'.format(person_dict['name'], str(person_dict['age']))
print(sentence)

# String formatting for the repeating value substitution for string formatting
tag = 'h1'
text = 'This is a headline'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

# Access the values directly from the dict in placeholders
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person_dict)
print(sentence)

# Access the values directly from the object in placeholders for string formatting
class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person('Mani', 27)
p2 = person('Giri', 47)

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# Named palceholders
sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='33')
print(sentence)

# Unpacking the dict values for string fomatting
sentence = 'My name is {name} and I am {age} years old.'.format(**person_dict)
print(sentence)

# Formatting numbers for a string
for i in range(1,11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

# Formatting numbers for a string -> print three (or n) digits for every number
for i in range(1,11):
    sentence = 'The value is {:03}'.format(i)
    print(sentence)

# Print n digits of a floating number-> Ex:2
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

# comma separator for numbers
sentence = '1MB is equal to {:,.2f} bytes'.format(1000*2) #Here {:,.2f} provides both comma separation and added two decimal places
print(sentence)

# Formatting datetime
import datetime
my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)
print(my_date)

# String formatting a date
sentence = '{:%B %d %Y}'.format(my_date) # Here %B->Month string(like September) %d->Day in date %Y->full year
print(sentence)

# Format like this-> March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)