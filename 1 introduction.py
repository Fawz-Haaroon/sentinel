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

#STRING-OPERATORS:- Escape Sequence Operator
# some escape characters include \n,\b,\t,\\,\ooo,\xhh,
# \a,\f,\r,\v
print("I am Jaspreet and \nI am \x66rom \Indi\141\".")
#Output
'''
I am Jaspreet and 
I am from \India".
'''

#STRING-OPERATORS:- Formatting Operator (format specifiers)
'''
String formatting operator (%) is used to format a string
%d, %c, %s, %f are some commonly used string formatters
'''
age = 28
print('My age is %d' %(age))
#Output
'''
My age is 28
'''

#String slicing with the THIRD parameter
user = 'I am jaspreet'
print(user[0:8:2])
# Output
'''
'Ia a'
'''

s = 'abc' * 3
print(s)
print(s[::3])
print(s[1::3])
print(s[:5:3])
#Output
'''
abcabcabc
aaa
bbb
aa
'''

# Negative THIRD parameter
s = 'I am Jaspreet'
print(s[8:1:-2])
#Output
'''
pa a
'''
# reversing a string
print(s[::-1])
#output
'''
teerpsaJ ma I
'''

# String Interpolation or String formatting
'''
the process of inserting an object into a predefined string is called string interpolation or string formatting
'''
# multiple variable interpolation
name = 'fawz'
city = 'chennai'
print("My name is %s and I live in %s." % (name,city))
#Output
'''
My name is fawz and I live in chennai.
'''

# str.format() function
name = 'Fawz'
city = 'Chennai'
print("My name is {} and I live in {}".format(name,city))
#Output
'''
My name is Fawz and I live in Chennai
'''

# Referencing variables though indexing
name = 'Fawz'
city = 'chennai'
print("My name is {0} and I live in {1}".format(name, city))
#Output
'''
My name is Fawz and I live in chennai
'''

# using keywords to refer for improving readability
n = 'Fawz'
c = 'Chennai'
print("My name is {name} and I live in {city}".format(name=n,city=c))
#Output
'''
My name is Fawz and I live in Chennai
'''

print("I got {0:f}% marks {2:f}% marks and {1:f}% in each term on English.".format(55.66,75.7768978989,56.99))
#Output
'''
I got 55.660000% marks in English.
'''

print("I GOT {0:.5f} in english , {1:.7f} in maths".format(94.566,98.45656767867867878))
#output
'''
I GOT 94.56600 in english , 98.4565677 in maths
'''

#fstrings
name = 'Fawz'
city = 'chennai'
print(f"My name is {name} and I am {city}")
print(F"My name is {name} and I am {city}")
#Output
'''
My name is Fawz and I am chennai
My name is Fawz and I am chennai
'''

#Calling methods of string is also possible
name = "FAWZ"
city = "Delhi"
print(f'My name is {name.upper()} and I live in {city.upper()}')
#output
'''
My name is FAWZ and I live in DELHI
'''

# for better readability multiline f-strings can be used
name = 'FAWZ'
age = 34
gender = 'male'
# 1st way - using backslash
intro1 = f"my name is {name}." \
                 f"my age is {age}." \
                 f"my gender is {gender}."
# 2nd way - using brackets
intro2 =( f"my name is {name}."
                 f"my age is {age}."
                 f"my gender is {gender}.")
# 3rd way - using triple quotes (everything including newlines and spaces are preserved in the format when this method is used)
intro3 = f'''my name is {name}
my age is {age}
my gender is {gender}'''

print(intro1)
print(intro2)
print(intro3)
#Output
'''
my name is FAWZ.my age is 34.my gender is male.
my name is FAWZ.my age is 34.my gender is male.
my name is FAWZ
my age is 34
my gender is male
'''




# IMPLICIT TYPE CONVERSION
'''
Ability of Python to convert an OBJECT from ONE Dat type to another without any intervention from the programmer

RULE OF CONVERSION : 
             LOWER Datatype is converted to the HIGHER Data type
The type of resultant depends upon the OPERATOR and 
VALUE WITH HIGHER DATA TYPE
'''

print(5 + 10.98)
# Output 
'''
15.98
'''
'''
integer value 5 is converted to float while giving result in order to be added with a float datatype(higher datatype)
'''
print(10/2)
# Output 
'''
2.00
'''
'''
division by its very nature always results in a floating type value
'''


# EXPLICIT TYPE CONVERSION
'''
refers to the conversion of OBJECT of ONE TYPE to ANOTHER TYPE
via Programmer's intervention
'''

# converting to int(value, base)
x = '110'
x = int(x,2)   
''' base 2 means, python treats it as binary balue and not decimal'''
print(type(x))
print(x + 1)

# output
'''
<class 'int'>
7
'''



# converting to float(value)
x = 78
x = float(x)
print(x)
#output
'''78.0'''
y = '78.54654580'
y = float(y)
print(y)
#outpyt
'''78.5465458'''

# converting to str(value)
a = 198
a = str(a)
print(type(a))
#output
'''<class 'str'>'''















