# range() fuction
'''
>>> SYNTAX:- range(start, stop, step)
                     |      |     |
                     ▼      |     ▼
starting position of the    |  specifies the increment value
sequence. Default value     |  Default value is 1
is 0.                       |
                            ▼
             Stopping position of the sequence. 
             Never included in the result of 
             the range() function
'''

# POINTS TO REMEMBER
'''
>>> the range() function only works with INTEGER AREGUMENTS
>>> all THREE ARGUMENTS can be POSITIVE or NEGATIVE
>>> the step value CANNOT be 0
'''

for i in range(5):
               print(i)
print('done')
#output
'''
0
1
2
3
4
done
'''

for i in range(1,10,2):
        print(i)
print('done')
#output
'''
1
3
5
7
9
'''


# Sum of first 'n' natural number using for loop
n = int(input('Enter the value of n : '))
sum = 0
for i in range(1, n+1):
        sum += i
print(f'sum of first {n} natural numbers is {sum}. ')
#output
'''
Enter the value of n : 5
sum of first 5 natural numbers is 15.
'''


## REVERSING  a range of numbers

# reversing a range of numbers using NEGATIVE STEP value
for i in range(5, 0, -1):
        print(i)
print('done')
#output
'''
5
4
3
2
1
done
'''

# reversing a range of numbers using reversed() function
for i in reversed(range(1, 6, 1)):
        print(i)
print('done')
#output
'''
5
4
3
2
1
done
'''






# ACCESSING CHARACTERS of a string using for loop
name = 'John'
for c in name:
    print(c, end=' ')    #extra argument to print the characters in the same line
#output
'''
J o h n
'''


# ITERATING  a string in REVERSE order using for loop (SLICING can be used for reversing)
name = 'John'
for c in name[::-1]:# iteration for reversing
    print(c, end=' ')
# output
'''
n h o J
'''


# ACCESSING WORDS pf a string using for loop ( split() function can be used to split a string into words)
sentence = 'Hello its a nice day to go out'
count = 0
for word in sentence.split():
    count += 1
print(f'There are {count} words in the sentence.')
#output
'''
There are 8 words in the sentence
'''


## using for loop with LISTS

# ITERATING over a list using for loop
cars = ['Audi', 'BMW', 'Benz']
for car in cars:
       print(car)
#output
'''
Audi
BMW
Benz
'''

# using for loop along with range() to iterate over a list
cars = ['Audi', 'BMW', 'Benz']
for i in range(len(cars)):
       print(cars[i])
#output
'''
Audi
BMW
Benz
'''

# for loop in LIST COMPREHENSION
cars = ['Audi', 'BMW', 'Benz']
[print(car) for car in cars]
#output
'''
Audi
BMW
Benz
'''


##for loop in DICTIONARY

# ITERATING over a dictionary using for loop 
course = {'name':'Python', 'instructor':'Jaspreet'}
for x in course:
    print(x)
#Output:
'''
name
instructor
'''


# ACCESSING VALUES of a Dictionary using for loop
#(square bracket notation can be used)
course = {'name':'Python', 'instructor':'Jaspreet'}
for x in course:
    print(course[x])
#output
'''
Python
Jaspreet
'''
#(values() method can be used)
course = {'name':'Python', 'instructor':'Jaspreet'}
for y in course.values():        #( (values() provides the VALUE of EACH key of the dictionary in the form of a LIST)
    print(y)
#output
'''
Python
Jaspreet
'''

# ACCESSIMG KEYS  of a Dictionary using for loop
course = {'name':'Python', 'instructor':'Jaspreet'}
for x in course.keys():         #(   keys() return the KEYS of the dictionary in the form of a LIST)
       print(x)
#output
'''
name
instructor
'''

# ACCESSING KEYS and VALUES of a Dictionary usinf for loop
course = {'name':'Python', 'instructor':'Jaspreet'}
for x, y in course.items():
       print(x, y)
#output
'''
name Python
instructor Jaspreet
'''





# for loop with else block
'''
> the else block will be executed only then the loop is NOT terminated 
  abruptly by the break keyword

>>> (eg)
sequence = 'abcefg'
for var in sequence:
       # statement inside for
else:
       # statement inside else

'''

fav_languages = ['Python', 'C', 'Java', 'Ruby']
for language in fav_languages:
       if language == 'Java':
              print('I like Java')
              break
else:
    print('I dont like Java')
# output
'''
I like Java
'''

# break and continue statements in for loop

# break statement
'''
> used to terminate the running loop
'''

numbers = list(range(0,100))
for number in numbers:
    if number >50:
        break
    print(number, end=' ')
#output
'''
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 
'''

while True:
    num = input('Enter the number(q for quit): ')
    if num == 'q':
        break
    print(num)
# output
'''
number(q for quit): 9
9
Enter the number(q for quit): q

'''


# continue statement
'''
> used to skip the current iteration of the loop
'''
for i in range(5):
      if i == 2 or i == 4:
            continue
      print(i)
#output
'''
0
1
3
'''

n = 0
while n <= 10:
      n += 1
      if n % 2 != 0:
            continue
      print(n, end=' ')
#output
'''
2 4 6 8 10 
'''


# NESTED FOR LOOP
list1 = [1,2,3]
list2 = [4,5,6]
for i in list1:
    for j in list2:
          print(i,j)
    print( )
#output
'''
1 4
1 5
1 6

2 4
2 5
2 6

3 4
3 5
3 6

'''


# NESTED WHILE LOOP
list1 = [1,2,3]
list2 = [4,5,6]
i = 0 
while i < len(list1):
    j = 0                   # written inside while, so as to reinitialize j to 0 
    while j < len(list2):
        print(list1[i], list2[j])
        j += 1
    print( ) 
    i += 1
#output
'''
1 4
1 5
1 6

2 4
2 5
2 6

3 4
3 5
3 6

'''




