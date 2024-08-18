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

#STRING METHODS
# strip() method
'''
HELPS IN REMOVING LEADING AND TRAILING CHARCACTERS WHICH WE MENTION TO DO SO (removes white spaces by default if nothing is mentioned)
> IT WILL NOT REMOVE MIDDLE CHARACTERS, ONLY CHECKS FOR THE CHARACTER AND REMOVES IT IF IT APPEARS IN THE BEGINNING OR END
'''
print('   I am Fawz    '.strip())
print('$$$ $$I am Fawz$$$$'.strip('$'))
#output
'''
I am Fawz
 $I am Fawz
'''

print('Hello world'.strip('ldoH'))
'''
   IN THIS CASE , STRIP METHOD CHECKS FOR THE OCCURANCE OF THE CHARACTERS MENTIONED.. STARTING FROM THE BEGINNING, AND STOPS WHEN A NON-MENTIONED CHARACTER OCCURS. AND THEN IT STARTS CHECKING FROM THE END FOR THE MENTIONED CHARACTERS AND STOPS IN WHEN A NON-MENTIONED CHARACTER OCCURS. IT WONT AFFECT THE OCCURENCE OF MENTIONED CHARACTER IF THEY APPEAR IN THE MIDDLE
'''
#output
'''
ello wor
'''

# lstrip() method
'''
ONLY CHECKS FOR LEADING CHARACTERS AND DOESNT AFFECT TRAILING ONES
'''
# rstrip() method
'''
ONLY CHECKS FOR TRAILING CHARACTERS AND DOESNT AFFECT LEADING ONES
'''


# split() method
'''
used to split string into a list (from left to right)

>>> SYNTAX
str.split(separator,maxsplit)

separator - represents the character where split should occur
maxsplit - represents the no. of splits. for 'n' splits we get 'n+1' items
(split() starts reading and separating the string from the left)
'''
print("Hello!$I$am$Jaspreet".split('$',maxsplit=2))
# output
['Hello','I','am$Jaspreet']


# rsplit() method
'''
used to split string into a list (from right to left)

>>> SYNTAX
str.rsplit(separator,maxsplit)

(split() starts reading and separating the string from right)
'''
print("Hello!$I$am$Jaspreet".rsplit('$',maxsplit=2))
# output
['Hello!$I','am','Jaspreet']
 


# join() method
'''
Used to JOIN the ELEMENTS of an 
ITERABLE (list, dictionary, tuple, set,string,)

>>>SYNTAX
separator.join(iterable)
'''

li = ['H','E','L','L','O']
print(''.join(li)) 
'''
       here '' is the separator, nothing, not even white space, and
       list li is used since its an iterable, and hence can be joined
'''
#OUTPUT
'''HELLO'''

d = {'name': 'ADAM' , 'country': 'US'}
print(' and '.join(d)) 
'''
       here ' and ' is the separator and dictionary d is used since its an iterable, and hence can be joined
'''
#Output
''''
name and country
'''


# replace() method
'''
used to replace a specific string with another string.

>>>SYNTAX
str.replace(oldString, newString, count)
'''
s = 'I LOVE TO EAT MANGO and MANGO and MANGO'
print(s.replace('MANGO','APPLE'))
print(s.replace(' ','_',4))
#Output
'''
I LOVE TO EAT APPLE and APPLE and APPLE
I_LOVE_TO_EAT_MANGO and MANGO and MANGO
'''



# upper() method
'''
used to convert all letters of the string to UPPERCASE

>>>SYNTAX
string.upper()
'''

# lower() method
'''
used to convert all letters of the string to LOWERCASE

>>>SYNTAX
string.lower()
'''

# capitalize() method
'''
returns a string where the first character of the first word is UPPERCASE, and rest remaind the same

>>>SYNTAX
string.lower()
'''

# isupper() method
'''
returns 'True' if ALL characters are uppercase, otherwise returns 'False'. so result is boolean value.

>>>SYNTAX
string.isupper()
'''

# islower() method
'''
returns 'True' if ALL characters are lowercase, otherwise returns 'False'. so result is boolean value.

>>>SYNTAX
string.islower()
'''


# isalpha() method
'''
returns 'True' if ALL characters(it checks even for white spaces) are ALPHABETS (a-z or A-Z)

>>>SYNTAX
string.isalpha()
'''
print("hello2".isalpha())
print("Hello I am Fawz".isalpha())
print("hshejgrhjsbhjs".isalpha())
#Output
'''
False
False
True
'''

# isnumeric() method
'''
returns 'True' if ALL characters(it checks even for white spaces or symbols like +,.,-, etc) are NUMBERS

>>>SYNTAX
string.isnumeric()
'''
print("3453453".isnumeric())
print("3453.4434".isnumeric())
print("2/4".isnumeric())
#Output
'''
True
False
False
'''

# isalnum() method
'''
returns 'True' if all characters are alphanumeric (a-z , A-Z, 0-9)
and no other characters
'''
print("353hjb".isalnum())
print(" my age is 9".isalnum())
#Output
'''
True
False
'''


# count() method
'''
returns the No. of occurences of a substring
if substring NOT FOUND, returns 0

>>>SYNTAX
string.count(substring, start index, end index)
so searches from start index till end index, the no. of occurences
'''
print("i love fruits, Fruits are healthy".count('fruits'))
print("i love fruits, Fruits are healthy".count('fruits', 3, 13))
#Output
1
1

# find() method
'''
returns the INDEX of the FIRST occurence of the substring
if substring NOT FOUND, returns -1

>>>SYNTAX
string.find(substring, start index, end index)
'''
print("Python is a beautiful language".find('b'))
print("Python is a beautiful language".find('b', 1, 5))
#Output
'''
12
-1
'''

# rfind() method
'''
returns the INDEX of the LAST occurence of the substring
if substring NOT FOUND, returns -1

>>>SYNTAX
string.rfind(substring, start index, end index)
'''
print("Python is a beautiful language".rfind('e'))
print("Python is a beautiful language".rfind('e', 1, 5))
#Output
'''
29
-1
'''


# index() method
'''
returns the INDEX of the FIRST occurence of the substring
if substring is NOT FOUND , it raises an EXCEPTION(valueError)

>>>SYNTAX
string.index(substring, start index, end index)
'''
print("Python is a beautiful language".index('e'))
print("Python is a beautiful language".index('e',1,5))
#Output
'''
13
ValueError: substring not found
'''

# rindex() method
'''
returns the INDEX of the LAST occurence of the substring
if substring is NOT FOUND , it raises an EXCEPTION(valueError)

>>>SYNTAX
string.rindex(substring, start index, end index)
'''
print("Python is a beautiful language".rindex('e'))
print("Python is a beautiful language".rindex('e',1,5))
#Output
'''
29
ValueError: substring not found
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




# LISTS (single and multi dimentional)

li = [ 1,2,3,4]
print(li[3])
#Output
'''
4
'''
Li = [[1,2,3], 'srdrf' ,[4,3,5,5,4,3]]
print(Li[2][3])
print(Li[1][3])
#Output
'''
5
r
'''

## Adding elements to a list

# append() method
'''
used to add items at the END of the list
'''
list = ['c', 'cpp', 'java']
list.append('python')
list.append('java')
list.append('javascript')
list.append(['html','css'])
print(list)
#output
'''
['c', 'cpp', 'java', 'python', 'java', 'javascript', ['html', 'css']]
'''

# insert() method
'''
used to add an item at specific position
SYNTAX:-  list.insert(position,value)
'''
List = ['html','css','javascript']
List.insert(1,'python')
print(List)
#Output
'''
['html', 'python', 'css', 'javascript']
'''

# extend() method
list1 = ['C', 'php', 'java', 'python']
list2 = ['html','css','javascript']
list1.extend(list2)
print(list1)
print(list2)
#Output
'''
['C', 'php', 'java', 'python', 'html', 'css', 'javascript']
['html', 'css', 'javascript']
'''



# input a list using loop
n = int(input('Enter the no. of items: '))
items = []
for i in range(n):
    x = int(input())
    items.append(x)
print(items)
# Output
'''
Enter the no. of items: 4
4
67
75
8
[4, 67, 75, 8]
'''

# creating a list using split() method
numbers = input('enter the numbers: ').split()
print(numbers)
#output (notics the output is recieved as string)
'''
enter the numbers: 43 34 33
['43', '34', '33']

'''



# Accepting a list using both
# split() and for loop


n = int(input('Enter the no. of items: '))
numbers = input('enter your ' + str(n) + ' numbers :' ).split()

print(numbers)

for i in range(0, n):
    numbers[i] = int(numbers[i])
    print(numbers)
    
print(numbers)
# Output
'''
Enter the no. of items: 4
enter your 4 numbers :33 99 77 66
['33', '99', '77', '66']
[33, '99', '77', '66']
[33, 99, '77', '66']
[33, 99, 77, '66']
[33, 99, 77, 66]
[33, 99, 77, 66]

'''


# changing or altering MULTIPLE ITEMS of a list
list = [ 34,345,'josh','java',455,'llm']
list[2:4] = ['review','python', 4543]
print(list)
#output
'''
[34, 345, 'review', 'python', 4543, 455, 'llm']
'''


# inserting NEW item in a list
'''
>>>SYNTAX:-  list.insert(index,item)
'''
list = ['java','python',45,54,'C']
list.insert(2,'mike')
print(list)
#output
'''
list = ['java','python','mike',45,54,'C']
'''


# removing item from list

# using remove() method -- (pass the string)
list = ['mike', 'java', 'kjhg']
list.remove('java')
print(list)
#output
'''
['mike', 'kjhg']
'''

# using pop() method --- (pass the index) list.pop(index) also returns the deleted item 
list = ['mike', 'java', 'snake']
print(list.pop(1))
print(list)
'''
IF NO INDEX IS SPECIFIED IN li.pop(index) INDEX , THEN THE LAST ITEM IS REMOVED
'''
#output
'''
java
['mike', 'snake']
'''

# using del keyword
li = ['mike', 'snake', 433, 543]
del li[1]
print(li)
#output
'''
['mike', 433, 543]
'''
# we can also delete ENTIRE list usinf del keyword
del li
print(li)
#output
'''
NameError: name 'li' is not defined
'''

# using clear method --- used to remove items of the list, and make an empty list
list = ['mike', 'java', 'kjhg']
list.clear()
print(list)
#output
'''
[]
'''

# Using LIST COMPREHENSION to shorten a for loop

  # (eg1) using a usual for loop
names = ['James', 'Joseph', 'Samuel', 'Jaguar', 'Ryan']
J_names = []
for name in names:
   if 'J' in name:
      J_names.append(name)
      print(J_names)
print(J_names)
#OUTPUT
'''
['James']
['James', 'Joseph']
['James', 'Joseph', 'Jaguar']
['James', 'Joseph', 'Jaguar']
'''
  # using LIST COMPREHESION
names = ['James', 'Joseph', 'Samuel', 'Jaguar', 'Ryan']
J_names = [name for name in names if 'J' in name]
print(J_names)
#OUTPUT
'''
['James', 'Joseph', 'Jaguar']
'''


  # (eg1) using a usual for loop 
animals = ['lion', 'tiger', 'whale', 'elephant', 'frog']
new_animals = []
for animal in animals:
   new_animals.append(animal.title())
   print(new_animals)
print(new_animals)
#OUTPUT
'''
['Lion']
['Lion', 'Tiger']
['Lion', 'Tiger', 'Whale']
['Lion', 'Tiger', 'Whale', 'Elephant']
['Lion', 'Tiger', 'Whale', 'Elephant', 'Frog']
['Lion', 'Tiger', 'Whale', 'Elephant', 'Frog']
'''
  # using LIST COMPREHENSION
animals = ['lion', 'tiger', 'whale', 'elephant', 'frog']
new_animals = [animal.title() for animal in animals ]
print(new_animals)
#OUTPUT
'''
['Lion', 'Tiger', 'Whale', 'Elephant', 'Frog']
'''


