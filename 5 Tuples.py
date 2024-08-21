# TUPLES TUPLES TUPLES

'''
>>> SYNTAX:- tuple_name = ( item1,item2, item3)
> Tuples are IMMUTABLE ( no changes can be made to the items of tuple)
> Tuple items are ordered with index and the order cannot be changed
> Tuples can have DUPLICATES
> Tuple is only recognised by a COMMA, even if it has only 1 ITEM
'''

# LENGTH of a tuple
car = ('AUDI', 'BENZ', 'BMW')
print(len(car))
#output
'''
3
'''

# TUPLE CONSTRUCTOR (alternative way to create tuple)
cars = tuple(('AUDI', 'BENZ', 'BMW'))  # needs two pairs of paranthesis
print(cars)
# output
'''
('AUDI', 'BENZ', 'BMW')
'''


## ACCESSING TUPLE ITEMS

# accessing Tuple items through POSITIVE INDEXING
cars = ('audi','benz','bmw')
print(cars[1])
#output
'''
benz
'''

# accessing Tuple items through NEGATIVE INDEXING
cars = ('audi','benz','bmw')
print(cars[-1])
#output
'''
bmw
'''

# accessing a RANGE of items using SLICING
cars = ('audi','benz','bmw')
print(cars[0:1])
print(cars[1:2])
print(cars[0:])
print(cars[:2])
print(cars[:])
#output
'''
('audi',)
('benz',)
('audi', 'benz', 'bmw')
('audi', 'benz')
('audi', 'benz', 'bmw')
'''



## UPDATING/ ADDING items to a TUPLE

'''
> its NOT possible to add items DIRECTLY to a tuple as tuples are IMMUTABLE
>>> we can Convert TUPLE --> LIST for this purpose
'''

# ADDDING ITEMS 
cars = ('Audi','BMW','Benz')
print(cars)
Lcars = list(cars)
Lcars.append('Toyota')
print(Lcars)
cars = tuple(Lcars)
print(cars)
#output
'''
('Audi', 'BMW', 'Benz')
['Audi', 'BMW', 'Benz', 'Toyota']
('Audi', 'BMW', 'Benz', 'Toyota')
'''

# UPDATING ITEMS
cars = ('Audi','BMW','Benz')
print(cars)
Lcars = list(cars)
Lcars[1] = 'FERRARI'
print(Lcars)
cars = tuple(Lcars)
print(cars)
#output
'''
('Audi', 'BMW', 'Benz')
['Audi', 'FERRARI', 'Benz']
('Audi', 'FERRARI', 'Benz')
'''

# REMOVING ITEMS
## using .remove())
cars = ('Audi','BMW','Benz')
print(cars)
Lcars = list(cars)
Lcars.remove('BMW')
print(Lcars)
cars = tuple(Lcars)
print(cars)
#output
'''
('Audi', 'BMW', 'Benz')
['Audi', 'Benz']
('Audi', 'Benz')
'''
## using del keyword <TO REMOVE ENTIRE TUPLE>
##(NO NEED TO CONVERT TO LIST CAN BE DONE DIRECTLY TO TUPLE)
cars = ('Audi','BMW','Benz')
del cars
print(cars)
#output
'''
NameError: name 'cars' is not defined
'''



# UNPACKING A TUPLE
'''
> Packing means Assigning values to a tuple
> Unpackiing means Extracting values of a tuple
  and assign them to variables
'''

cars = ('Audi','Mercedes','BMW')
car1, car2, car3 = cars
print(car1)
print(car2)
print(car3)
#output
'''
Audi
Mercedes
BMW
'''

# Use of ASTERISK in unpacking a tuple
'''
> used when the numbers of variables are less than the
  values of a tuple
'''

# >( when asterisk is USED IN THE LAST VARIABLE, the remaining items of the tuple are Assigned to the last variable,and RETURNED WITHIN [])
cars = ('Audi','Mercedes','BMW','Ford','Lambo')
car1, car2, *car3 = cars
print(car1)
print(car2)
print(car3)
#output
'''
Audi
Mercedes
['BMW', 'Ford', 'Lambo']
'''

# >( If asterisk is used with a variable other than the last variable, then the values are assigned until the VALUES LEFT Matches the VARIABLES LEFT)
cars = ('Audi','Mercedes','BMW','Ford','Lambo')
car1, *car2, car3 = cars
print(car1)
print(car2)
print(car3)
#output
'''
Audi
['Mercedes', 'BMW', 'Ford']
Lambo
'''