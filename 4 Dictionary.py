# DICTIONARIES DICTIONARIES DICTIONARIES
# DICTIONARIES IN PYTHON


# MUTATION (changing values) in dictionary

dictionary = {'car': 'Audi', 'model': 'V7'}
dictionary['model'] = 'V8'
print(dict)
# output
'''
{'car': 'Audi', 'model': 'V8'}
'''

'''
SAME KEY SHOULD NOT BE USED, IF USED THEN THE VALUE OF THE LATTER'S VALUE WILL BE UPDATED TO THE KEY
'''


# LENGTH of dictionary
dictionary = {'brand':'Audi' , 'model': 'V7'}
print(len(dictionary))
#output
'''
2
'''

# ALTERNATIVE WAY to construct dictionary using  dict() CONSTRUCTOR
car = dict(brand = 'Audi', model = 'V8')
print(car)
#output
'''
{'brand': 'Audi', 'model': 'V8'}
'''


## ACCESSING DICTIONARY ITEMS

# accessing VALUES using KEY NAMES
cars = {'brand':'Audi' , 'model': 'V7'}
print(car['brand'])
#output
'''
Audi
'''

# accessing VALUES using get() method
cars = {'brand':'Audi' , 'model': 'V7'}
print(cars.get('brand'))
#output
'''
Audi
'''

# accessing KEYS using keys() METHOD
cars = {'brand':'Audi' , 'model': 'V7'}
print(cars.keys())
cars['fuel'] = 'petrol'
print(cars.keys())
#output 
#[RETURNS A 'VIEW-OBJECT' (e.g) dict_keys([]) Containing 'KEYS' as a LIST]
# view-object also REFLECTS ANY CHANGES done to the dictionary
'''
dict_keys(['brand', 'model'])
dict_keys(['brand', 'model', 'fuel'])
'''

# accessing VALUES using values() method
cars = {'brand':'Audi' , 'model': 'V7'}
print(cars.values())
cars['fuel'] = 'petrol'
print(cars.values())
#output
#[RETURNS A 'VIEW-OBJECT' (e.g) dict_values([]) Containing 'values' as a LIST]
# view-object also REFLECTS ANY CHANGES done to the dictionary
'''
dict_values(['Audi', 'V7'])
dict_items([('brand', 'Audi'), ('model', 'V7'), ('fuel', 'petrol')])
'''

# accessing values using items() method
cars = {'brand':'Audi' , 'model': 'V7'}
print(cars.items())
cars['fuel'] = 'petrol'
print(cars.items())
#output
#[RETURNS A 'VIEW-OBJECT' (e.g) dict_itemsontaining KEY-VALUE pair
# view-object also REFLECTS ANY CHANGES done to the dictionary
'''
dict_items([('brand', 'Audi'), ('model', 'V7')])
dict_items([('brand', 'Audi'), ('model', 'V7'), ('fuel', 'petrol')])
'''



## CHANGING and ADDING dictionary items

# Changing VALUES usimg KEYNAMES
car = {'brand':'audi', 'model':'q7'}
car['model'] = 'f6'
print(car)
#output 
'''
{'brand':'audi', 'model':'f6'}
'''

#Changing VALUES using update() method
# >> SYNTAX:- dict_name.update(key-newvalue)
car = {'brand':'audi', 'model':'q7'}
car.update({'model':'s5'})
print(car)
#output
'''
{'brand': 'audi', 'model': 's5'}
'''

# ADDING NEW ITEMS using KEY NAMES
car = {'brand':'audi', 'model':'q7'}
car['color'] = 'black'
print(car)
#output
'''
{'brand': 'audi', 'model': 'q7', 'color': 'black'}
'''

# ADDING NEW ITEMS using update() method
car = {'brand':'audi', 'model':'q7'}
car.update({'color':'black'})
print(car)
#output
'''
{'brand': 'audi', 'model': 'q7', 'color': 'black'}
'''




## REMOVING items of a dictionary

# REMOVING an ITEM using pop() method
# >> SYNTAX:- dict_name.pop(key)
car = {'brand':'audi', 'model':'q7'}
print(car.pop('model'))
print(car)
#output (pop() RETURNS THE DELETED VALUE)
'''
q7
{'brand': 'audi'}
'''

# REMOVING an ITEM using popitem() method
'''
removes the last inserted item
returns the deleted item as tuple
'''
#>> SYNTAX:- dict_name.popitem()
car = {'brand':'audi', 'model':'q7'}
print(car.popitem())
print(car)
#output
'''
('model', 'q7')
{'brand': 'audi'}
'''

# REMOVING an ITEM using del keyword
car = {'brand':'audi', 'model':'q7'}
del car['model']
print(car)
#output
'''
{'brand': 'audi'}
'''

# REMOVING A DICTIONARY using del keyword
car = {'brand':'audi', 'model':'q7'}
del car
print(car)
#output
'''
NameError: name 'car' is not defined
'''

# EMPTY (not delete) using clear() method
#>> SYNTAX:- dict_name.clear()
car = {'brand':'audi', 'model':'q7'}
car.clear()
print(car)
#output
'''
{}
'''



## COPYING A DICTIONARY

# Copying using copy() method
# >>SYNTAX:- dict2 = dict1.copy()
car = {'brand':'audi', 'model':'q7'}
car_copy = car.copy()
print(car_copy)
print(car)
car_copy['model'] = 'f5'
print(car_copy)
print(car)
# OUTPUT
'''
--- # a copy is made ---
{'brand': 'audi', 'model': 'q7'}
{'brand': 'audi', 'model': 'q7'}
--- # changes to the copy didnt affect the original dict ---
e original dict ---
{'brand': 'audi', 'model': 'f5'}
{'brand': 'audi', 'model': 'q7'}
'''

#copying using dict() method
# >> SYNTAX:- dict2 = dict(dict1)
car = {'brand':'audi', 'model':'q7'}
car_copy = dict(car)
print(car)
print(car_copy)
car_copy['model'] = 'h9'
print(car_copy)
print(car)
#OUTPUT
'''
--- # a copy is made ---
{'brand': 'audi', 'model': 'q7'}
{'brand': 'audi', 'model': 'q7'}
--- # changes to the copy didnt affect the original dict ---
{'brand': 'audi', 'model': 'h9'}
{'brand': 'audi', 'model': 'q7'}
'''
