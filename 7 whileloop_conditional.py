# simple while loop
n = 1
while n <= 3:
    print(n)
    n += 1
#output
'''
x is False
'''


# sum of 'n' Nartural numbers using while loop
n = int(input('enter the value of n '))
sum = 0                         # initializing the variable
while n > 0:
    sum += n
    n -= 1
print(f'Sum is {sum}')
# output
'''
enter the value of n 9
Sum is 45
'''


# infinite while loop
'''
n = 100
while True:
    print(n)
    n -= 1
'''

 
while True:
    line =input("Enter the line (type 'q' to quit): ")
    if line == 'q':
        break
    print(line)
#output
'''
Enter the line (type 'q' to quit): 
hello
Enter the line (type 'q' to quit): q
     
'''


# while loop with else
'''
(lets consider a list of fruits that includes 4 types of fruits,
 WAP to determine whether if th fruit 'orange' is present or not)
'''
# 1st method
fruits = ['apple', 'banana', 'mango', 'strawberry']
fruits_len = len(fruits)
index = 0

fruit_found = False

while index < fruits_len:
    if fruits[index] == 'orange':
        fruit_found = True
        print('orange is available.')
        break
    index += 1

if not fruit_found:          # if fruit_found remains False, not returns True, so executes statement
    print('orange is not available')


#2nd method
fruits = ['apple', 'banana', 'mango', 'strawberry']
fruits_len = len(fruits)
index = 0
while index < fruits_len:
    if fruits[index] == 'orange':
        print('orange is available.')
        break
    index += 1
else:
    print('orange is not available')

