# Python

# Line Structure in Python
>口 Python code is divided into __logical lines__.

>口 Every line is ended by a token called newline.(i.e) Python uses new lines to complete a command.\
  (as opposed to other programming languages which often use semicolons or parentheses).

>口 Python relies on indentation, using whitespace, to define scope (a block of code); such as the scope of 
   loops,functions and classes.\
   (unlike other programming languages that often use curly bracket for this purpose).


→ So a single __logical line__ can consist of one or more __physical lines__.\
→ we can add 2 __physical lines__ into 1 __logical line__ by using \ 

    a = 1\
    + 2
    
→ we can also have 2 __logical lines__ in 1 __physical line__ using ;

    x = 1 ; y = 2

## Python Indentation

>• __Indentation__ refers to the __spaces__ at the beginning of a code line.\
>• Python uses indentation to indicate a block of code.\
>• Python will give you an error if you skip the indentation.\
>• You have to use the __same number of spaces__ in the same block of code,\
   otherwise Python will give you an error.

# Keywords in Python
><img src= "image1.png" width= 430px height=210px >

# Data classes(types) in Python
><img src= "image2.png" width= 430px height=210px >

Variables can store data of different\
 types and different types can do different things
><img src= "image3.png" width= 400px height=240px >

## Getting the Datatype of an object

 You can get the datatype of any object by using the **type()** function\
 (ALL DATATYPES ARE ILLUSTRATED BELOW)
 

>[!TIP]
>x = str("Hello World")\
print(type(x))
>
>## #<class 'str'>

>[!TIP]
>x = int(20)\
print(type(x))
>
>## #<class 'int'>

>[!TIP]
>x = float(20.5)\
print(type(x))
>
>## #<class 'float'>

>[!TIP]
>x = complex(1j)\
print(type(x))
>
>## #<class 'complex'>

>[!TIP]
>x = list(["apple", "banana", "cherry"])\
print(type(x))
>
>## #<class 'list'>

>[!TIP]
>x = tuple(("apple", "banana", "cherry"))\
print(type(x))
>
>## #<class 'tuple'>

>[!TIP]
>x = range(6)\
print(type(x))
>
>## #<class 'range'>

>[!TIP]
>x = {"name" : "John", "age" : 36}  **(OR)**\
x = dict(name="John", age=36)\
print(type(x))
>
>## #<class 'dict'>

>[!TIP]
>x = set({"apple", "banana", "cherry"})\
print(type(x))
>
>## #<class 'set'>

>[!TIP]
>x = frozenset({"apple", "banana", "cherry"})\
print(type(x))
>
>## #<class 'frozenset'>

>[!TIP]
>x = bool(5)\ **(OR)**\
x = True\
print(type(x))
>
>## #<class 'bool'>

>[!TIP]
>x = b"Hello"  **(OR)**\
x = bytes(5)\
print(type(x))
>
>## #<class 'bytes'>

>[!TIP]
>x = bytearray(5)\
print(type(x))
>
>## #<class 'bytearray'>

>[!TIP]
>x = memoryview(bytes(5))\
print(type(x))
>
>## #<class 'memoryview'>

>[!TIP]
>x = None\
print(type(x))
>
>## #<class 'NoneType'>

> [!IMPORTANT]
>### BASED ON FLOATS
><img src= "image.png" width= 390px height=100px >

> [!IMPORTANT]
>### FEW ESCAPE SEQUESCES 
> | sequence | use |
>| --- | --- |
>| \n | used for newline |
>| \a | used for alert sound |
>| \b | for backspace character |
>| \f | for form feed |
>| \r | for carriage return |
>| \t | tab space horizontal |
>| \v | tab space vertical |
>| \ooo | character of octal value oo |
>| \xHH | character of Hexa decimal value HH |

# PYTHON OPERATORS
## ● Arithmetic Operators
 Arithmetic operators are used with numerioc values to perform common mathematical operations
 | Operation | Operator Symbol | Description |
 | --- | --- | --- |
 | Addition | + | to add |
 | Subtraction | - | to subtract |
 | Multiplication | * | to multiply |
 | Division | / | to divide |
 | Modulus | % | Reminder |
 | Floor Division | // | Quotient |
 | Exponent | ** | Raise to a Power |
## ● **Assignment Operators**
 Assignment operators are used to assign values to variables
 | Operation | Operator Symbol | Description
 | --- | --- | --- |
 | Assig | = | to assign a value |
 | add and assign | += | to add both operands and assign the result to left operand|
 | subtr and assign | -= | to subtract both operands and assign the result to left operand |
 | multiply and assign | *= | to multiply both operands and assign the result to left operand |
 | divide and assign | /= | to divide both operands and assign the result to left operand |
 | Modulus and assign | %= | to perform modulus both operands and assign the result to left operand |
 | Exponent and assign | **= | to exponentiate the left operant by right operand and assign the result to left operant |
 | Floor and assign | //= | perfom floor division and assign the value to the left operand| 
 | Bitwise AND and assign | &= | find bitwise AND and assign value to left operant|
 | Bitwise OR and assign | \|= | find bitwise OR and assign value to left operand|
 | Bitwise XOR and assign | ^= | find bitwise XOR and assign value to left operand|
 | Bitwise right-shift and assign | >>= | find bitwise RIGHSHIFT and assign value to left operand |
 | Bitwise left-shift and assign | <<= | find bitwise LEFTSHIFT and assign value to left operand|
## ● **Comparison Operators**
 Comparison operators used to compare 2 different values
 | Operation | Operator Symbol |
 | --- | --- |
 | Equal to | == |
 | Not Equal to | != |
 | Less than | < |
 | Less than or Equal | <= |
 | Greater than or Equal | > |
 | Greater than or Equal | >= |
## ● **Logical Operators**
 Logical operators are used to combine conditional statements.
 | Operation | Operator Symbol | Description |
 | --- | --- | --- |
 | Negate condition | not | returns the end result of the expression opposite to what is evaluated (False means it returns True, True means it returns False) |
 | Either condition | or | to check if any of the given expressions are true, then it returns result as TRUE. if all the expressions are false, then returns result as FALSE |
 | Both condition | and | to check if every expression given is true ,then it returns result as TRUE. even if any 1 of the expression is false, it returns result as FALSE |
>[!NOTE]
><img src="image4.png">
## ● **Identity Operators**
 Logical operators are used to compare the objects, not if they are equal, but if they are actually the same object.
 >SYNTAX :-    
 > id(object)
## ● **Membership Operators**
 Membership operators are used to test if a sequenceis present in an object.\
There are 2 membership operators

> in

> not in
## ● **Bitwise Operators**
 Bitwise operators are used to compare (binary) numbers.\
 ### Types
 >  BITWISE AND (&)\
 >  BITWISE OR (|)\
 >  BITWISE NOT (~)\
 >  BITWISE XOR (^)\
 >  BITWISE RIGHT-SHIFT\
 >  BITWISE LEFT-SHIFT\
>(all theoritical knowledge of performing these operations are written in notes pen-paper for my understanding)
 


> [!IMPORTANT]
>## Precedence and Associativity
>### **PRECEDENCE**
> tell the order in which operations should be performed
on operands in an expression
><img src="image5.png" width="400px">
>### **ASSOCIATIVITY**
>tells the order of evaluation of the operators with same precedence in an expression
 >| Oprators | Associativity |
 >| --- | --- |
 >| () | Left to Right |
 >| ** | Right to Left |
 >| +x and -x | Left to Right |
 >| *, /, //, %  | Left to Right |
 >| + and - | Left to Right |


## Difference between **for loop** and **while loop**
 | **for loop** | **while loop** |
 | --- | --- |
 | for loop needs an **iterable object** to iterate | while loop executes based on some conditions |
    for var in iterable:
         # do something 

    while condtion:
         # do something
 | **for loop** | **while loop** |
 | --- | --- |
 | for loop is known when no. of interations is known in advance | while loop is i used when no. of iterations is not known in advanced |
    for i in range(1, 6):
            print(i)
    
    # OUTPUT
    0
    1
    2
    3
    4
    5



    while True:
        n = input('Enter the number: ')
        if n == 'q':
             break
        print(n)
    
    # OUTPUT
    Enter the number: 5
    5
    Enter the number: q


 | **for loop** | **while loop** |
 | --- | --- |
 | Both for loop and while loop can run infinite times | Both for loop and while loop can run infinite times |

    items = [0]
    for item in items:
    print(item)
    items.append(item)

    #OUTPUT
    0
    2
    3
    4
    5
    0
    2
    3
    4
    5
    .
    .
    .
    .(REPEATED)

    item = 0
    while True:
        print(item)
    
    #OUTPUT
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    (0, 1, 2, 3, 4, 5)
    .
    .
    .
    .(REPEATED)
