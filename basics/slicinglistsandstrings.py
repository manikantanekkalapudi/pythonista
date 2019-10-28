'''Slicing Lists and Strings in Python

Slicing helps us to get the required substring from string and element(s) in list
'''

# Declaring a list of numbers
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index->  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# -ve->  -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# Accessing an element with +ve index
print(my_list[5])

# Accessing an element with -ve index
print(my_list[-3])

# List slicing has 3 parameters that can be used for the purpose-> start, end and step
# list_name[start:end:step] -> start index is inclusive and end index is exclusive
print(my_list[0:5])

# Below print statements will print the same
print(my_list[3:8])
print(my_list[-7:-2])

# +ve and -ve indices
print(my_list[1:-2])

print(my_list[2:]) #This will print from 2nd index till the end of the list

print(my_list[:6]) #This will print from 0th index till 6th index but not sixth

# Step will allow us to skip certain number of elements
print(my_list[2:8:2]) #This will skip every alternative element in the list till index 8 and index 8 is not inclusive

# -ve step ->This is possible only with -ve indices
print(my_list[2:8:-1]) #In this case it'll try to print empty list because the slicing will happen in +ve index direction and the step is happening in -ve index direction

# -ve step with -ve indices
print(my_list[-2:-8:-2]) #This will print the resulting list and the end index is excluded

# Reverse the list using a string
print(my_list[::-1])

# Reversing a string
word = 'Manikanta Nekkalapudi'
print(word[::-1])

# Slicing a string is similar to the list
print(word[:4])