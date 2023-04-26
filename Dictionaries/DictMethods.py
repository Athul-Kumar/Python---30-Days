
"""
                        DICTIONARIES METHODS

                    1.Creating a Dictionary

a.using {} brackets

syntax

empty_dict = {}

b.using dict() built-in function

syntax

empty_dict = dict()

c.Dictionary with data values

dicts = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

                    2.Dictionary Length

len() --> using len function we can find the length of the dictionary

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4

                3.Accessing Dictionary Items

a.accessing dictionary items by referring to its key name

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4

b.get() --> Accessing an item by key name raises an error if the key does not exist.
            To avoid this error first we have to check if a key exist or we can use the get method.
            The get method returns None, which is a NoneType object data type, if the key does not exist.

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct.get('key1))

                    4.Adding item to a dictionary

a)
syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

dct['key5'] = 'value5'

b) update() --> The update() method will update the dictionary with the items from a given argument.
                If the item does not exist, the item will be added.

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.update({'key5':'value5'})

5.Modifying items in a dict(mutable)

a)

syntax
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'

b.update() --> like adding item to dict we can use update to change item from dict
syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.update({'key2':'value10'})

6.checking keys in a dictionary

using in operator

syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print('key1' in dct)

7.Removing key and value pairs from a dictionary

a.pop(key) --> emoves the item with the specified key name:

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key2') #removes key2

b.popitem() --> removes the last item, return as a tuple

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dcr.popitem()
removes the last item from the dict

c.del --> removes an item with specified key name

syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct['key2'] #remove key 2

        8.changing dict to a list of items

items() --> The items() method changes dictionary to a list of tuples.

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct.items()) #dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

            9.clearing a dictionary

clear() --> clear all item from the dict, return type none

syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

print(dct.clear()) #None

        10.Deleting a Dictionary

del keyword --> deletes dictionary completely
syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct

11. copying a dict

copy() --> copy a dictionary using a copy() method.
             Using copy we can avoid mutation of the original dictionary.

syntax

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

dct_copy = dct.copy() #{'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}

12. dict items as list

a.dict keys as a list --> The keys() method gives us all the keys of a a dictionary as a list.

syntax
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys) # dict_keys['key1', 'key2', 'key3', 'key4']

b.dict values as a list --> The values method gives us all the values of a a dictionary as a list.

syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values) $ dict_values(['value1', 'value2', 'value3', 'value4']

"""


# creating dictionary

# 1.using {}

empty_dict = {}
print(type(empty_dict))

# 2.using dict() function

empty_dicts = dict()

print(type(empty_dicts))

# 3.dictionary with values

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

# The dictionary above shows that a value could be any data types:
# string, boolean, list, tuple, set or a dictionary.

# 2.finding the length of the dictionary


anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

print(len(anime_char)) #7

# 3.a) accessing dict items using keys

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}


print(anime_char['skills'])  #accessing key skills
print(anime_char['address']['street'])  #accessing first item in dict address
print(anime_char['country'])
# print(anime_char['phone']) #raised an error cause the key not present

# 3.b) get ()

print(anime_char.get('first_name'))
print(anime_char.get('address'))
print(anime_char.get('phone')) # phone is not in dict so it returned none value

# 4.adding item to a dict


anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
    'street': 'death street',
    'zipcode':'dd-rrr'
    }

}

# adding phone number to dict - anime_char
# a)
anime_char['phone'] = 9747045868

print(anime_char)

# 4.b) update()

anime_char.update({'death': '13-11-1997'})
print(anime_char)

# 5 modifying item in a dictionary

# a)

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

anime_char['country'] = 'South Korea'
print(anime_char)

# another example modyifying last name to kira

anime_char['last_name'] = 'kira'
print(anime_char)

# 5.b using update()

# changing first_name to levi
anime_char.update({'first_name':'levi'})
print(anime_char)

# 6.checking item in dict

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

print('first_name' in anime_char) #true
print('age' in anime_char) #true

# 7.removing key and value pairs from a dict

# a. pop(key)

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

# removing age from anime_char

anime_char.pop('age')
print(anime_char)

# b.popitem()

# removed last item from the dict

print(anime_char.popitem()) #type --> tuple
print(anime_char)

# c.del keyword
# removing key: value --> country(key)
del anime_char['country']
print(anime_char)

# 8.changing dict to a list of items


anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}


dic_list = anime_char.items()
print(dic_list)

# 9.clearing a dict

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

# clearing all the items froma dict

print(anime_char.clear())
print(anime_char)  #{}


# 10.deleting the dict

del anime_char
# print(anime_char)

# 11. copy()

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

copy_dict = anime_char.copy()

print(copy_dict) #copy of dict anime_char
print(anime_char) #orginal dict

# 12.
# a.dict values as a key

anime_char = {

    'first_name' : 'Light',
    'last_name'  : 'Yagami',
     'age'  : 25,
    'country' : 'japan',
    'is_married' : True,
    'skills': ['serial killer', 'police officer', 'student'],
    'address':{
        'street': 'death street',
        'zipcode':'dd-rrr'
    }

}

keys = anime_char.keys()
print(keys)
print(type(keys))

# b.dict values as values

values = anime_char.values()
print(values)
print(type(values))
