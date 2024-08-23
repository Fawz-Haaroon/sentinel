# FUNCTIONS IN PYTHON
'''
- (Reusability) block of reusable code to perform specific task
- (Modularity) helps in breaking down a program into smaller and manageable pieces, easier to understand and maintain
- SYNTAX 
def function_name(parameters):
        # code to be executed
        # .....
        return result
'''
# Function declaration
def square(number):
    result = number ** 2
    return result
# Caling the Function to execute it
num = 5
result_square = square(num)
# statement to print the output
print("The square of", num, "is", result_square)
#OUTPUT
'''
The square of 5 is 25
'''



 
# DOCSTRING in a function
''' a comment used inside a function to document it, 
    it describes what a piece of code can do. 
  - it is written within triple quotes.
'''
## Printing a docstring
'''
use the ( __doc__ ) attribute 
to access the Docstring of  a specific function
'''
def greet(name):
    """This function greet the person"""
    print('HELLO,' + name + '!')
print(greet.__doc__)
#OUTPUT
'''
This function greet the person
'''



# CALL STACK
'''
- the Call Stack is used by the program to keep track of function calls ( it helps the program decide which function should be executed in which order)
- the Call Stack is made up of STACK FRAMES, One for Each function call.
'''

def foo(x,y):
    x = x-y
    return x
def caller():
    x = 4
    y = 10
    print(x,y)
    z = foo(x+1, y+3)
    print(x,y,z)
caller()
# Output
'''
The square of 5 is 25
This function greet the person
'''

# functions with positional arguments
def greet(name,age):
    """This function greets the person and tells the age"""
    print(f"Hello, {name}! You're {age} years old.")
greet('Alice', 30)
#OUTPUT
'''
Hello, Alice! You're 30 years old.
'''


# function with default arguments
def greet(name, greeting = "Hello"):
    print(greeting  + "," + name + "!")
greet("ALICE")
greet("bob", "HI")
#OUTPUT
'''
Hello,ALICE!
HI,bob
'''


# funcions with keyword arguments
def greet(name, greeting, punctuation):
    print(greeting + "," + name + punctuation)
#using keyword arguments to pass values to the function
greet(punctuation="!", greeting="HELLO", name="Neso")
#OUTPUT
'''
HELLO,Neso!
'''


# ORDER of Arguments
'''
KEYWORD arguments comes only after positional arguments
'''
def simple_interest(P, R=1, T=1):
    return (P * R * T) / 100
print(simple_interest(10, T=3))  #(simple_interest(T=3, 10) is wrong since keyword argument is coming before positional argument, so python throws an error)
# OUTPUT
'''
0.3
'''



def generate_squares(limit):
    squares = [i ** 2 for i in range(limit)]
    return squares

limit= 5                   #this is declared outside the function and is different from the parameter variable, and hence is used as an argument
result = generate_squares(limit)
print(result)
#OUTPUT
'''
[0, 1, 4, 9, 16]
'''


# returning multiple results is also possible
def math(a,b):
    return a+b, a-b, a*b
sum , diff, product = math(4,5)
print(sum, diff, product)
#OUTPUT
'''
9 -1 20
'''


# returning a tuple ( when only one variable is given to store multiple return results)
def math(a,b):
    return a+b, a-b, a*b
result = math(4,5)
print(result)
#OUTPUT
'''
(9, -1, 20)
'''


# returning a list ( the return value is enclosed in [square brackets]within which multiple return results are stored.this will be returned as list)
def math(a,b):
    return [a+b, a-b, a*b]
result = math(4,5)
print(result)
#OUTPUT
'''
[9, -1, 20]
'''


# returning a dictionary
def math(a,b):
    values = {'sum': a+b, 'diff': a-b, 'product': a*b}  # creating a dictionary
    return values
result = math(4,5)
print(result)
#OUTPUT
'''
{'sum': 9, 'diff': -1, 'product': 20}
''' 


def rect_area(length,breadth):
    if length<=0 or breadth<=0:
        return None
    else:
        area = length * breadth
        return area
length , breadth = 30, 10       #this is declared outside the function and is different from the parameter variable, and hence is used as an argument
area = rect_area(length, breadth)

if area is None:
    print(" Invalid dimensions ")
else:
    print(f"Area: {area}")
#OUTPUT
'''
Area: 300
'''


import math

def circle_area(radius):
    area =  math.pi * radius**2
    check = area > 100
    return check
result = circle_area(6)
print(f'Is the circle area greater than 100?  {result}.')
#OUTPUT
'''
Is the circle area greater than 100?  True.
'''



# FUNCTION ENCAPSULATION
'''
- The ability to HIDE IMPLEMENTATION DETAILS by Wrapping
  an inner function within the outer function
- Making the inner function inaccessaible outside the outer function
'''


# Closure in python
'''
- its A NESTED function, that allowws Accessing the variables from the outer function (from the enclosing scope)
  even after the outer function completes its execution (leaves the call stack)
'''

def outer_function(x):
    def inner_function():
        print(x)
    return inner_function

inner = outer_function(10)      # when this is done, the definition of the called function is kept, and only the reference to inner_funcion iis returned, and this reference,,,,
inner()         # reference to the inner_function is received by this variable, so when called this variable as method, we can use the inner_function
#OUTPUT
'''
10
'''

# uses of closures
'''
- Helps in creating resusable functions with different behaviours.
'''
def multiplier(factor):
    def multiply(x):
        return x* factor
    return multiply
multiply_by_2 = multiplier(2)
multiply_by_3 = multiplier(3)

print(multiply_by_2(50))   # argument for the inner function is given when called through the variable
print(multiply_by_2(33))
# OUTPUT
'''
100
99
'''



# Assigning FUNCTIONS to VARIABLES   ( since everything in python is considered an OBJECT, even function can be assigned to a variable)

# function definition
def greet(name):
    return f"Hello, {name}!"

# Assigning te function to a variable
my_function = greet  # jus name of the function is mentioned, since we are not calling the function, we are just referencing(assigning) the function to the variable, so no need for '()'

# using the variable to call the function
result = my_function('Jaspreet')
print(result)
#OUTPUT
'''
Hello, Jaspreet!
'''

# Advantages of assigning functions to variables
'''

'''