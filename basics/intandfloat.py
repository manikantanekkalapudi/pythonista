'''Integers and Float in Python
Integer-> Whole number
Float-> Decimal number
Video-> https://youtu.be/khKv-8q7YmY
'''

# Integer variable

num = 3

# Print type of the variable-> int in this case
print(type(num))

# Float in this case
num = 33.4
print(type(num))

# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
# Arithmetic Operators:
# Addition:       3 + 2
# Subtraction:    3 - 2
# Multiplication: 3 * 2
# Division:       3 / 2
# Floor Division: 3 // 2
# Exponent:       3 ** 2
# Modulus:        3 % 2

# Floor division
print(3//2) # Prints 1

# Python follows BODMAS rule for solving expressions


# Increment
num += 1 # Increments by 1. Similarly for decrement->num -= 1, product-> num *= 1. 

# Absolute value
print(abs(-21))

# Round-> second parameter represents the digits to rounded after decimal
print(round(3.14179, 3)) #O/p: 3.142

# Source: https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Ints/snippets.txt
# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

# Numbers in the form of strings

num1 = '100'
num2 = '200'

print(num1+num2) #Prints the concatenated version of the 2 string i.e., 100200

# Casting strings to integers
print(int(num1)+int(num2)) #O/p: 300