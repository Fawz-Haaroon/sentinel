# LISTS LISTS LISTS
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
