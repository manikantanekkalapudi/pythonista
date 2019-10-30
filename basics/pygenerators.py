'''Generators in Python- How to use them and the benefits you receive
video-> https://youtu.be/bD05uGo_sVI
'''

# Current method
def square_nums(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_nums([1, 2, 3, 4])
print(my_nums)

# Using generators. We'll use 'yeild' keyword at the end of the function
def square_nums_gen(nums):
    for i in nums:
        yield i*i

# Following line prints generator object instead of numbers
print(square_nums_gen([1, 2, 3, 4]))

my_nums = square_nums_gen([1, 2, 3, 4, 5])
print(next(my_nums)) # Prints 1
print(next(my_nums)) # Prints 4
print(next(my_nums)) # Prints 9
print(next(my_nums)) # Prints 16
print(next(my_nums)) # Prints 25
print(next(my_nums)) # 'StopIteration' exception is thrown because the generator is exhausted of the values

# List comprehension
my_nums = [x*x for x in [1, 2, 3, 4, 5]]

# Generator comprehension
my_nums = (x*x for x in [1, 2, 3, 4, 5]) # One value is stored at a time



'''
Source: https://realpython.com/introduction-to-python-generators/
Generator functions are a special kind of function that return a lazy iterator. 
These are objects that you can loop over like a list. 
However, unlike lists, lazy iterators do not store their contents in memory only one item at a time.
Generator functions use the Python yield keyword instead of return.

'yield' indicates where a value is sent back to the caller, but unlike return, you don’t exit the function afterward.

Note:
Using yield will result in a generator object.
Using return will result in returning the single object.

Example:
def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_sequence()
next(gen)
o/p -> 0
next(gen)
o/p -> 1
next(gen)
o/p -> 2
next(gen)
o/p -> 3

nums_squared_lc = [num**2 for num in range(5)]
o/p -> [0, 1, 4, 9, 16]
nums_squared_gc = (num**2 for num in range(5))
o/p -> <generator object <genexpr> at 0x107fbbc78>

# Memory consumption
import sys
nums_squared_lc = [i * 2 for i in range(10000)]
sys.getsizeof(nums_squared_lc)
o/p -> 87624
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))
o/p -> 120
In this case, the list you get from the list comprehension is 87,624 bytes, while the generator object is only 120. This means that the list is over 700 times larger than the generator object!
There is one thing to keep in mind, though. If the list is smaller than the running machine’s available memory, then list comprehensions can be faster to evaluate than the equivalent generator expression.

yeild:
When the Python yield statement is hit, the program suspends function execution and returns the yielded value to the caller.
(In contrast, return stops function execution completely.) When a function is suspended, the state of that function is saved.
This includes any variable bindings local to the generator, the instruction pointer, the internal stack, and any exception handling.
This allows you to resume function execution whenever you call one of the generator’s methods.

'''

