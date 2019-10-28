'''List Comprehensions in Python'''

# Declaring a list of numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Declaring an empty list my_nums to copy the elements from nums
my_nums = []

# for loop to copy the elements from nums to my_nums
for num in nums:
    my_nums.append(num)

print(my_nums)

# List comprehension for the above copy operation
my_nums = [num for num in nums]
print(my_nums)

# Copy sqaures of each element from nums to my_nums using list comprehension
my_nums = [num*num for num in nums]
print(my_nums)

# Using map and lambda-> Anonymous function
my_nums = list(map(lambda n: n/2, nums))
print(my_nums)

# if condition in list comprehensions
my_nums = [num for num in nums if num%2 == 0]
print(my_nums)

# if condition using filter and lambda
my_nums = list(filter(lambda num: num%2 == 0, nums))
print(my_nums)

# Generate a (letter, num) pair for each letter in 'abcd' and each number in '0123
# Using for loop
my_list = []
for letter in 'abcd':
    for num in range(0,4):
        my_list.append((letter, num))
print(my_list)
print('*'*50)

# Above (letter, num) pair using list comprehensions
my_list = [(letter, num) for letter in 'abcd' for num in range(0,4)]
print(my_list)

# Zip function-> Dictionary Comprehensions. Zip function will create key-value pair for the corresponding elements in the list
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# Zip object when passed to dict will create a key value pairs for corresponding elements from both lists
print(dict(zip(names, heros)))

# Zip object when passed to list will create a tuple for corresponding elements from both lists
print(list(zip(names, heros)))

# Using dict comprehensions
superheros = {name:hero for name, hero in zip(names, heros)}
print(superheros)

# Dict comprehensions with if condition
superheros = {name:hero for name, hero in zip(names, heros) if name != 'Peter'}
print(superheros)

# Set comprehensions
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = {n for n in nums}
print(my_set) #Sets will never have duplicate values by property

# Generator functions
def gen_func(nums):
    for n in nums:
        yield n * n

# Both the lines will generate the same input
# my_gen = gen_func(nums)
my_gen = (n*n for n in nums)

for i in gen_func(nums):
    print(i)

