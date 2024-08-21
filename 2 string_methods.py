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

>>> separator - represents the character where split should occur
>>> maxsplit - represents the no. of splits. for 'n' splits we get 'n+1' items
>>> (split() starts reading and separating the string from the left)
'''
print("Hello!$I$am$Jaspreet".split('$',maxsplit=2))
# output
'''
['Hello','I','am$Jaspreet']
'''

# rsplit() method
'''
used to split string into a list (from right to left)

>>> SYNTAX
str.rsplit(separator,maxsplit)

(split() starts reading and separating the string from right)
'''
print("Hello!$I$am$Jaspreet".rsplit('$',maxsplit=2))
# output
'''
['Hello!$I','am','Jaspreet']
'''


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