# IF conditional statement
# elif conditions
# else conditions
# NESTED if conditionals

'''
# USUAL condition format

if condition1:
    # executed when condition1 is True
    if condition1A:
        # executed when condition2 is True, only if condition1 is True
    # statement outside nested if block (2nd statement of 1st if condition)
elif condition2:
    # executed when condition1 is not satisfied, if satisied, the elif is skipped
else:
    # executed in the case where none of the conditions are satisfied

'''


# shorthand if else format ( used when 1 IF STATEMENT AND 1 ELSE STATEMENT  alone is needed to be executed)
'''
>>> executed statement | if | condition | else | statement
'''
age = 6
print('age is greater than 5') if age > 5 else print('age is less than 5')
# Output
'''
age is greater than 5
'''


# eg with logical AND
age = 20
nationality = 'American'
if age > 18 and age <30 and nationality == 'Indian':
    print('You are Eligible for exam and fee is ₹1500')
elif age > 18 and age <30 and nationality == 'American':
    print('you are Eligible for the exam and fee is $50')
else:
    print('not eigible')
# output
'''
you are Eligible for the exam and fee is $50
'''


# eg with logical OR
today = 'tuesday'
if today == 'saturday' or today == 'sunday':
    print('its a holiday')
elif today == 'monday' or today == 'tuesday':
    print('work 2 hrs extra')
else:
    print('normal work hours')
# output
'''
normal work hours
'''


# eg with logical NOT

a = False
if not a:
    print('x is False')
#output
'''
a is False
'''

name = 'John'
if not name:
    print('No name.')
else:
    print(f"Yourname is {name}.")
#output ( if the string is empty, then the NOT operator returns True, else False)
'''
Your name is John
'''

names = ['John','Mike','Sarah']
if not names:
    print('No names')
else:
    print(f"There are a total of {len(names)} names.")
#output
'''
There are a total of 3 names.
'''