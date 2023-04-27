
"""
                                    Array methods

                                    1.creating an array

Array in Python can be created by importing array module.
array(data_type, value_list) is used to create an array with data type and value list specified in its arguments.

                                    2.Adding elements to an array

1.insert() --> insert one or more data elements into array based on required position.

syntax

arr = ['item1','item2'item3']

arr.insert(position, value)

2.append() -->used to add the value to the end of the array

arr = ['item1','item2'item3']
arr.append(value)

                        3.Accessing elements from the array

In order to access the array items refer to the index number.
Use the index operator [ ] to access an item in a array.
The index must be an integer.

syntax

arr = ['item1','item2'item3']
arr[0] = item1


                        4.Removing elements from the array

a.remove() --> only removes one element at a time.
            ( Remove method in List will only remove the first occurrence of the searched element.
                same in array)

syntax
arr = ['item1','item2'item3']

arr.remove(value) #removes the first occurence of the search element

b.pop() -->  by default it removes only the last element of the array,
            to remove element from a specific position of the array,
            index of the element is passed as an argument to the pop() method.

syntax

arr = ['item1','item2'item3']
arr.pop(positon, value)

                    5.slicing the range of elements from the array

*  Slice operation is performed on array with the use of colon(:)
* To print elements from beginning to a range use [:Index]
* to print elements from end use [:-Index]
*  to print elements from specific Index till the end use [Index:]
*  to print elements within a range, use [Start Index:End Index]
*  to print whole array in reverse order, use [::-1].

                        6.searching element in array

index() --> returns the index of the first occurence of value mentioned in argument

syntax
arr = ['item1','item2'item3']
arr.index(1) = 'itme2'

                            7.updating elements in an array

In order to update an element in the array we simply reassign a new value to the desired index we want to update.

syntax

arr = ['item1','item2'item3']

arr[1] = 'item10'

                        8.count element in an array

count()

syntax

arr = ['item1','item2'item3', 'item1']
arr.count('item1')

                            9.Reversing elements in an array

reverse()

syntax

arr = ['item1','item2'item3', 'item1']
arr.reverse # ['item1','item3','item2', 'item1']

                        10.extend element from array

extend()

syntax
arr = ['item1','item2'item3', 'item1']
arr.extend(['item7','item8', 'item11'])

"""

# 1.creating an array of integers

import array as arr

a = arr.array('i', [1,2,3])

print("The newly created array is : ", end=" ")
for i in range(0,3):
    print(a[i], end= " ")
print()

# 2.creating an array of decimals

b = arr.array('d', [2.5, 3.2, 5.6])

print("The newly created array: ", end=" ")
for i in range(0,3):
    print(b[i], end=" ")
print()

# 2.adding values to the array

# a.insert()
import array as arr

c = arr.array('i', [1,2,3])

print("array before the insert method: ", end=" ")
for i in range(0,3):
    print(c[i],end=" ")
print()

# inserting value

c.insert(0,4)

print("array after insert method: ", end=" ")
for i in range(0,len(c)):
    print(c[i], end=" ")

print()

# append()
print("array before append method: ", end=" ")
for i in range(0, len(c)):
    print(c[i], end=" ")

# adding item using append method
c.append(99)
print("\n")
print("array after append method: ", end=" ")
for i in range(0, len(c)):
    print(c[i], end=" ")

print()

# 3.Accessing elements from the array

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print("accessing first element: ", a[0])

print("accessing 5th element: ", a[4])

# 4. Removing elements from the array

# a.remove

import array as arr

d = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

print("array before the remove method: ", end=" ")
for i in range(0, len(d)):
    print(d[i], end=" ")

print()

# removing item from the array using remove()

d.remove(7)

print("array after using remove method: ", end=" ")

for i in range(0, len(d)):
    print(d[i], end=" ")

print()

# b.pop()

print("array before the pop method: ", end=" ")
for i in range(0, len(d)):
    print(d[i], end=" ")

print()

# using pop method to remove item

# by default pop

d.pop()

print("after removing an  item using pop: ", end=" ")
for i in range(0, len(d)):
    print(d[i], end=" ")

# by using specific index

d.pop(0)
print('after removing first item:  ', end=" ")
for i in range(0, len(d)):
    print(d[i], end=" ")


#  5. array slicing

import array as arr

F = arr.array('i', [1,2, 3, 4, 5, 6, 7, 8, 9, 10])
print()
# printing initial array
print("printing initial array")
for i in range(0, len(F)):
    print(F[i], end=" ")

# slicing items from 2nd to 7th

sliced_array = F[1:7]
print(sliced_array)
# another example

another_sliced = F[6:9]
print(another_sliced)

# reverse array

reversed_array = F[::-1]
print(reversed_array)


# 6.search --> index()

import array

arr = array.array('i', [1, 2, 3, 1, 2, 5])

print("The new created array is : ", end="")
for i in range(0,len(arr)):
    print(arr[i], end=" ")

print()


# using search
print("after index: ", end=" ")
print(arr.index(1))
print(arr.index(3))


# updating index
import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])

print("array before the updation: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

print()

arr[3] = 12
print("array after the updation: ", end=" ")

for i in range(0, len(arr)):
    print(arr[i], end=" ")

print()

# counting item in array using count()

print("before count method: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

# count()

count = arr.count(2)
print("Number of occurence of 2 is :", count)

# reversing the array

arr.reverse()
print(arr)

# extend the array

# before extend
print("array before extend: ", end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")

arr.extend([100,200,300])

# after extend
print("\n")
print("array after extend: ",end=" ")
for i in range(0, len(arr)):
    print(arr[i], end=" ")