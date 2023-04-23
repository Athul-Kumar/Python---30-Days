
"""
                Methods or actions related to tuple
"""

"""

#  1. creating a tuple

# 1.creating an empty tuple
syntax

empty_tuple = ()
print(type(empty_tuple))
# 2.creating an empty tuple using tuple()

empty_tuple = tuple()
print(type(empty_tuple))

"""


# tuple with initial values

tuple_1 = ('item1', 'item2', 'item3')

print(tuple_1)

# another example

fruits = ('banana', 'apple', 'mango', 'lemon')
print(fruits)


"""
#        2. To find the length of a tuple
syntax

tpl = ('item1','item2','item3')
len(tpl)
"""

# example

print(len(fruits))

#  3.Accessing Tuple items

"""
        syntax

tpl = ('item1','item2','item3')

first_item = tpl[0]
last_index = len(tpl) -1
last_item = tpl[last_index]
        
 Negative indexing
 
 first_item = tpl[-3]
 last_item = tpl[-1]        
        
        
"""

# examples

fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruit = fruits[0]
print(first_fruit)

last_index = len(fruits) - 1
last_fruit = fruits[last_index]
print(last_fruit)

#  negative indexing

fruits = ('banana', 'orange', 'mango', 'lemon')

first_fruit = fruits[-4]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

#    4.slicing tuple

"""
We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, 
the return value will be a new tuple with the specified items.


range of positive indexes
Syntax

tpl = ('item1', 'item2', 'item3','item4')

print(tpl[:4] #all item
print(tpl[0:] #all item
middle_two_items = tpl[1:3] #it doesn't include item at index 3

Range of negative indexing

syntax

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]
middle_of_two = tpl[-3:-1]

"""

fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[0:]
all_fruits = fruits[:4]
orange_mango = fruits[1:3]
orange_to_rest = fruits[1:]

# negative indexing

fruits = ('banana', 'orange', 'mango', 'lemon')

all_fruits = fruits[-4:]
middle_two = fruits[-3:-1]
orange_to_rest = fruits[-3:]

"""
                    5.changing a tuple to list
We can change tuples to lists and lists to tuples. 
Tuple is immutable if we want to modify a tuple we should change it to a list.

syntax

tpl = ('item1', 'item2', 'item3','item4')
changing to list

lst = list(tpl)

"""

ipl_teams = ('CSK', 'MI', 'RR', 'LSG', 'KKR', 'SRH')

# changing to list

ipl_team_lists = list(ipl_teams)
print(type(ipl_team_lists))

print(ipl_team_lists[1]) #MI

# converting back to tuple

ipl_teams = tuple(ipl_team_lists)
print(type(ipl_teams))

"""
                6.checking an item in tuple
                
We can check if an item exists or not in a tuple using in, it returns a boolean.

syntax 

tpl = ('item1', 'item2', 'item3','item4')
'items2' in tpl #True

"""

# examples

ipl_teams = ('CSK', 'MI', 'RR', 'LSG', 'KKR', 'SRH')

print('RR' in ipl_teams)
print('DC' in ipl_teams)

"""
                            7.Joining Tuples
                

We can join two or more tuples using + operator

syntax

tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2

"""
# example

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')

fruit_and_veggies = fruits + vegetables
print(fruit_and_veggies)

"""
                            8.Deleting Tuples
                            
It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.

# syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1

"""

# example

fruits = ('banana', 'orange', 'mango', 'lemon')

del fruits
# print(fruits)

"""
                    9.count()

count method returns the number of occurence of a value, 

syntax
tpl1 = ('item1', 'item2', 'item3')
tpl1.count('item1') # returns 1 (1 item is present)


"""

football_palyers = ('CR7', 'LM10', 'Rashford')

print(football_palyers.count('CR7'))

"""
                        10.index()

it returns first index of value , if no value then return value error

syntax
tpl1 = ('item1', 'item2', 'item3')
tpl1.index('item3') #2(index value of item3 is 2)
"""

ipl_players = ('MSD','VK18','DK','ABD')

print(ipl_players.index('DK'))