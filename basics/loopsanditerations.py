''' Loops and Iterations - For/While Loops '''

# Looping through a list
nums = [1,3,4,5,63,4,8]

for num in nums:
    print(num)
print('*'*50) 
'''
Break-> Stops the loop completely and executes the later statements
Continue-> Stops the current iteration and continues the execution with next iteration
'''
# Break
for num in nums:
    if num == 5:
        print('Found!')
        break
    print(num)

print('*'*50)

# Continue
for num in nums:
    if num == 5:
        print('Found!')
        continue
    print(num)
print('*'*50)
# Range->The lower limit(start) in range is inclusive and upper limit(end) is exclusive. step is the interval between the consequtive numbers in the range
# range(start,end, step)
for i in range(0,10,2):
    print(i)
print('*'*50)
# While loop->it'll continue till the condition is False. The condition should be Flase at some point
x = 0
while x <= 10:
    print(x)
    x+=1
print('*'*50)

# Break statement in while loop
x = 0
while True:
    if x == 5:
        break
    print(x)
    x+=1
