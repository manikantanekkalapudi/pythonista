'''Namedtuple in Python - When and why should you use namedtuples?'''
# Importing namedtuple
from collections import namedtuple

# Declaration of a tuple-> representing an RGB value for color variable
color = (55, 155, 255)
print(color[0])

# Tuple can be very confusing and less informative about it's purpose and etc. after some time like 6 months
# So, dict
color = {'red':55, 'green':155, 'blue':255}
print(color['red'])

# A namedtuple is in b/w tuple and dict to represent data
Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(55, 155, 255)

print(color[0])

print(color.blue)