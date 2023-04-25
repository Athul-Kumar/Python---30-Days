"""
                                    SET METHODS

1.Creating a set --> a.empty_set = {}
                 --> b.empty_set = set()

    creating set with initial items
                --> st = {'item1', 'item2','item3', 'itme4'}

2.Getting sets length --> st = {'item1', 'item2','item3', 'itme4'}
                     --> len(st)

3.  ACCESSING ITEMS IN A SET --> Using loops

4.checking an item --> st = {'item1', 'item2','item3', 'itme4'}
                   --> print('item1' in st) #True

5.Adding items to a set --->

 a.Add() --> used to add one item to the set

 syntax

st = {'item1', 'item2','item3', 'itme4'}
st.add('item5')

b.update() --> used to add multiple items to a set, update takes list as argument

syntax
st = {'item1', 'item2','item3', 'itme4'}
st.update(['item5','item6','item7'])

6.Removing item from a set

a.remove ---> We can remove an item from a set using remove() method.
             If the item is not found remove() method will raise errors

syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item3')

b.discard ---> unlike remove(), discard method does not raise an exception when an element is missing
                from a set

syntax

st = {'item1', 'item2', 'item3', 'item4'}
st.discard('item4')

c.pop() --> removes item from set, doesn't take args cause set are un-ordered and un-indexed

syntax

st = {'item1', 'item2', 'item3', 'item4'}
st.pop() --> random item will be removed

7.Clearing item in a set

clear() --> removes all the elements from the set

syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()

8.Deleting a set

Using Del keyword we can delete the set

syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
set will de deleted

9. Copy a set (copy()) --> returns a shallow copy of a set

syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.copy()

10. converting list to set and viceversa

syntax

lst = ['item1', 'item2', 'item3', 'item4', 'item1']

st = set(lst)  # {'item2', 'item4', 'item1', 'item3'}
                - the order is random, because sets in general are unordered

11. Joining sets

a.update() --> Update This method inserts a set into a given set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)

b.Union() -->Union method returns new set

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)

12.Finding Intersection items --> returns a set of items which are in both the sets

syntax
st1 = {'item1','item2','item3','item4'}
st2 = {'item2','item3'}
st1.intersection(st2) #{'item2','item3'}

13.Checking subset and superset

A set can be subset or superset of the other sets

a.subset --> issubset() (reports whether another set containing this set)
syntax

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
b.superset --> issuperset() (reports whether this set contains another set)
syntax


st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st1.issuperset(st2)

14.checking the difference Between Two sets --> return the difference of two or more set as a new set

syntax
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2

15.Finding the symmetric difference between two sets --> It returns the the symmetric difference between two sets. It means that it returns a set that contains all items from both sets,
                                                        except items that are present in both sets,
                                                         mathematically: (A\B) ∪ (B\A)

syntax

# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}

16.checking two sets are joint or not -->
isdisjoint() --> if two sets do not have a common items or items we call them disjoint sets
if it True --> joint sets
if it False --> not a joint set
"""

# creating set

# 1.
empty_set = {}
# 2.
empty_sets = set()

print(empty_set)
print(empty_sets)

# creating set with initial items

sports_set = {'golf', 'football', 'cricket', '100 M'}
print(sports_set)

# getting length of a set

hollywood_actors = {'Tom halland', 'Tom cruise', 'Johnny depp', 'Brad pitt'}
print(len(hollywood_actors))

# 4.Checking items in a set

print(hollywood_actors)

print('Tom cruise' in hollywood_actors)  #True
print('De caprio' in hollywood_actors)  #False

# 5.Adding items to a set

#  a.add()

fruits = {'Apple', 'Banana', 'lemon', 'Orange'}

# adding jack fruit to fruits

fruits.add('Jack fruit')
print(fruits)

# adding multiple it's to a set
# b.update()

fruits.update(['papaya', 'Berry', 'avacados'])
print(fruits)

# Removing item from set

# a.remove()

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}

# removing 4th item

lap_brands.remove('apple')
print(lap_brands)

# raising key error if value is not present

# lap_brands.remove('hp')
# print(lap_brands)

# b.discard()

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}

# removing 5th item
lap_brands.discard('Dell')
print(lap_brands)

# checking if discard will raise key error

lap_brands.discard('APPLE')
print(lap_brands)

# c.pop()

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}
print(lap_brands.pop())
print(lap_brands)

# Clearing the set
# clear()

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}

lap_brands.clear()
print(lap_brands) #set will be empty

# deleting a set

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}

del lap_brands
# print(lap_brands) set is deleted

# copying a set

# copy()

lap_brands = {'HP', 'Lenovo', 'MSI', 'apple', 'Dell', 'Asus'}

brands = lap_brands.copy()
print(brands)


# converting list to set

fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']

fruits = set(fruits)
print(fruits)
print(type(fruits)) #only 4 items in set --> no duplicate items for set

# joining sets

# a.update

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# b.union

fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}

fruit_veg = fruits.union(vegetables)
print(fruit_veg)


# Finding Intersection Items

whole_numbers = {0,1,2,3,4,5,6,7,8,9,10}
even_numbers = {0,2,4,6,8,10}

common_numbs = whole_numbers.intersection(even_numbers)
print(common_numbs)  # returns --> {0,2,4,6,8,10}

# another example

python = {'p', 'y', 't', 'h', 'o', 'n'}
dragon = {'d', 'r', 'g', 'o', 'n'}

common_letters = python.intersection(dragon)
print(common_letters)


# checking subset and superset

# a.issubset

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(even_numbers.issubset(whole_numbers))
print(whole_numbers.issubset(even_numbers)) #because whole_number is superset of even number

# b.issuperset()

print(whole_numbers.issuperset(even_numbers)) #whole number is super set, even number is subset
print(even_numbers.issuperset(whole_numbers)) #False


# Checking difference between two set

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}

print(whole_numbers.difference(even_numbers)) # set1 / set2
print(even_numbers.difference(whole_numbers))   # set()

# another example


python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(dragon.difference(python))
print(python.difference(dragon))


# symmetric difference --> (a/b) U (b/a)

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}

print(whole_numbers.symmetric_difference(some_numbers))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.symmetric_difference(dragon)) #p,y,t,h U d,r,a,g = p, y, t, h, d, r, a, g


# checking two sets are joint or not

# isdisjoint()

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}

print(even_numbers.isdisjoint(odd_numbers)) #True no items to join two sets

# another example

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}

print(python.isdisjoint(dragon))  #False (o, n)