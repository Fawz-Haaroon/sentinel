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



 