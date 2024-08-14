import keyword
keyword.kwlist

print('hello world')

# working with multiple variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(z)
print(y)

'''
OUTPUT
apple
cherry
banana
'''


# difference between using global and function specific local variable
# when a variable with same name as global variable is defined inside a function differently, then when the function is called this local variable is taken as its value
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

'''
OUTPUT
Python is fantastic
Python is awesome
'''


# a global variable an be changed inside a function by using "global" keyword and assigning new value , it will be applied once the function is called 
# else the object will hold on to the original value. Once the funtion is called, the previous value of the variable wont be considered anymore

x = 'fantastic'
def myfunc():
  global x
  x = 'mouse'
  print("Python is " + x)
  
print("Python is " + x)  
myfunc()
print("Python is " + x)
 
'''
OUTPUT
Python is fantastic
Python is mouse
Python is mouse
'''

# Strings in python

name = 'Arifureta'
print(name[0])
#output
'A'

#STRINGS- Accessing substring of a string (slicing)
name = 'Haaroon'
print(name[0:7])
print(name[0:])
print(name[:7])
print(name[:])
print(name[-7:])
#output
'''
Haaroon
Haaroon
Haaroon
Haaroon
Haaroon
'''

#STRING-OPERATORS:- Concatenate Operator
a = 'aaaa'
b = 'bbbb'
c = 'cccc'
z = a + b + c 
print(z)
#output
'''
aaaabbbbcccc
'''

#STRING-OPERATORS:- Repitition Operator
x = 'Fawz'
print(x * 3)
print(x * 0)
print(x * -2)
#output
'''
FawzFawzFawz


'''

#STRING-OPERATORS:- Comparison Operator
'''
Comparisons are case sensitive, each character has an ASCII value  while using these operators, only the ASCII values are compared
ASCII value of A=65, B=66, C=67 ......
ASCII value of a=97, b=98, c=99 ......
so A < a
1] == 
2] != 
3] <
4] <=
5] >
6] >=
'''

#STRING-OPERATORS:- Membership Operator
'''
1] in 
>>> 'jas' in 'jaspreet'
True
2] not in
>>> 'p' not in 'jaspreet'
True
'''




 