
"""
                        Accessing List items Using positive Indexing

we access each item in a list using their index.A list index start from 0.
"""
animes = ['Dragon ball z', 'One piece', 'Naruto', 'Bleach', 'Breserker']

# accessing 2nd item in a list
second_anime = animes[1]
print(second_anime)
# accessing last anime in a list
last_anime = animes[4]
print(last_anime)

# another method for accessing last anime

last_index = len(animes)-1

last_anime_in_list = animes[last_index]
print(last_anime_in_list)


"""
                Accessing list items using Negative indexing
                
Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item.
"""

# examples

cars = ['Nissan GTR', 'Toyota Supra', 'Honda NSX-1000', 'RX-7']

last_car = cars[-1]
print(last_car)
first_car = cars[-4]
print(first_car)
second_car = cars[-3]
print(second_car)

# unpacking list

bikes = ['H2R', 'panigela', 'CBR', 'R1', 'rx', 'R15']

Ninja, Ducatti, Honda, *Yamaha = bikes

print(Ninja)
print(Ducatti)
print(Honda)
print(Yamaha)

countries = ['Germany', 'Mexico', 'Sudan', 'India', 'Japan', 'Korea']

europe, N_america, S_africa, *Asia = countries
print(europe)
print(N_america)
print(S_africa)
print(Asia)

"""
                        Slicing items from a list
                        
Positive Indexing: We can specify a range of positive indexes by specifying the start, end and step, the return value will be a new list.
(default values for start = 0, end= len(lst)-1 (last_item), step-1)

"""


anime_char = ['Naruto uzumaki', 'Monkey D Luffy', 'Asta', 'Light Yagami']

all_char = anime_char[0:4]
print(all_char)
allOfThem = anime_char[0:]
print(allOfThem)
luffy_Asta = anime_char[1:3]
print(luffy_Asta)
naruto_Asta = anime_char[::2]
print(naruto_Asta)

"""
Negative Indexing: We can specify a range of negative indexes by specifying the start, end and step, the return value will be a new list.

"""

anime_vill = ['Madara uchiha', 'Marine', 'Devil king', 'Shinigami']

all_vill = anime_vill[-4:]
print(all_vill)

marine_devil = anime_vill[-3:-1]
print(marine_devil)
madara_shinigami = anime_vill[-4::3]
print(madara_shinigami)
reversing = anime_vill[::-1]
print(reversing)


"""
                Modifying List

List is a mutable or modifiable ordered collection of items. 

"""

sports = ['cricket', 'football', 'tennis', 'Boxing']

sports[1] = 'Soccer'
print(sports)

# changing last item

last_index = len(sports)-1

sports[last_index] = 'UFC'
print(sports)


"""
                            Checking items in a list
                            
Checking an item if it is a member of a list using in operator
"""

organs = ['heart', 'lungs', 'eyes', 'liver', 'small intestine', 'pancreas']

does_exist = 'liver' in organs
print(does_exist) #True

does_exist = 'brain' in organs
print(does_exist)


"""
                        USEFUL LIST METHODS
                        
1.append --> append object to the end of a list

syntax --> lst = list()
            lst.append(item)
            
2.insert() -->  insert a single item at a specified index in a list. Note that other items are shifted to the right

syntax --> lst = ['item1','item2']
            lst.insert(index.item)
            
3.remove() -->  remove method removes a specified item from a list (remove first occurence of a value)

syntax --->  lst = ['item1','item2']
            lst.remove(item)
            
4.pop() ---> The pop() method removes the specified index, (or the last item if index is not specified)

syntax --> lst = ['item1', 'item2']
            lst.pop() --> removes last item by default
            lst.pop(index) --> removes item @ specific index
            
5.Del (del keyword)  --> The del keyword removes the specified index and it can also be used to delete items within index range. 
                        It can also delete the list completely
                        
syntax --->             lst ['item1','item2']
                        del lst[index]  #delete single item
                        del lst[start:end] #delete range of item
                        del lst   # delete list completely
                        
6.clear() ---> removes all items from a list(list will be empty)
lst = ['item1','item2']
lst.clear()


# imp  --> copying list = It is possible to copy a list by reassigning it to a new variable in the following way: 
          list2 = list1. Now, list2 is a reference of list1, any changes we make in list2 will also modify the original, list1. But there are lots of case in which we do not like to modify the original instead we like to have a different copy. 
           One of way of avoiding the problem above is using copy().
           
#7.copy() --> Returns the shallow copy of the list

syntax --->     lst = ['item1','item2']
                lst_copy = lst.copy()
                
#8.joining List -->
    a) plus Operator(+)
    b) extend() --> extend() method The extend() method allows to append list in a list.
    
        syntax   --> list1 = ['item1','itme2']
                     list2 = ['item3','item4']
                     list1.extend(list2)
                     
# 9.count() --> count() method returns the number of times an item appears in a list

syntax ---> lst = ['item1','item2']
            lst.count(item)
            
# 10.index() --> The index() method returns the index of an item in the list

syntax-->      lst = ['item1','item2']
                lst.index(item)
                
# 11.reverse() ---> method reverse the order of the list

syntax -->      lst = ['item1','item2']
                lst.reverse()
                
# 12 sort() ---> To sort lists we can use sort() method or sorted() built-in functions. 
                 The sort() method reorders the list items in ascending order and modifies the original list. 
                 If an argument of sort() method reverse is equal to true, 
                 it will arrange the list in descending order.
                 
syntax  --->  lst = ['item1','item2']
                lst.sort() #ascending
                lst.sort(reverse= True) #descending
"""

# 1.append
list_items =[]
list_items.append('pen')
print(list_items)
print(len(list_items))

list_items.append('pencil')
print(list_items)

# 2.insert()

frds_names = ['jithin', 'amar', 'ajmal']

frds_names.insert(2,'shaloof')
print(frds_names)
print(frds_names[2])

# 3.remove()

off_roads = ['mahindra thar', 'Tata ghurka', 'toyota prado', 'mahindra scorpio', 'tata safari', 'mahindra thar']

print(len(off_roads))

off_roads.remove('mahindra thar')
print(off_roads)
print(len(off_roads))

#4. pop()

print(off_roads)
off_roads.pop()
print(off_roads)
off_roads.pop(2)
print(off_roads)

#5.del keyword

malayalam_movies = ['romanjam', 'Driving license', 'Minnal murali', 'angamali diaries', 'premam']

del malayalam_movies[1]
print(malayalam_movies)
del malayalam_movies[1:3]
print(malayalam_movies)
del malayalam_movies
# print(malayalam_movies) #error pop up due to list was completely deleted

# 6.clear()

series = ['BB', 'GOT', 'walking Dead', 'Wednesday', 'All of us dead']

series.clear()
print(series) #list is empty after using clear()

# 7. copy()

anime_movies = ['your name', 'akira', 'weathering with you', '5 centimeters per seconds']

anime_movies_copies = anime_movies.copy()
print(anime_movies_copies)
print(anime_movies)

# 8.joining Lists

positive_numbers = [1,2,3,4,5]
negative_numbers = [-1,-2,-3,-4,-5]
zero = [0]

integers = positive_numbers + zero + negative_numbers
print(integers)

# extend() = extend() method The extend() method allows to append list in a list.

odd_numbers = [1,3,5,7,9]
even_numbers = [2,4,6,8,10]

odd_numbers.extend(even_numbers)
print(odd_numbers)

# another example

list_1 = ['A', 'E', 'I', 'O', 'U']
list_2 = ['B', 'C', 'D', 'F', 'G']

list_3 = []
list_3 = list_1.extend(list_2)
print(list_3)  #we can't assing the extend two list to new list

# 9.count()

fancy_numbs = [7, 13, 69, 99, 69, 10, 33, 77, 7, 777, 123, 111]

print(fancy_numbs.count(7))
print(fancy_numbs.count(13))

# 10.index()

juices = ['avacados', 'dates', 'lassi', 'orange', 'mango']

print(juices.index('orange'))
print(juices.index('dates'))

# 11.reverse()

print(juices)
juices.reverse()
print(juices)
numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbs.reverse()
print(numbs)

# 12.sort()

numb_list = [10, 90, 40, 59, 99, 1001, 23, 54]

numb_list.sort()
print(numb_list)
numb_list.sort(reverse=True)
print(numb_list)


# sorted() = method that returns the ordered list without modifying the original list

fruits = ['banana', 'orange', 'mango', 'lemon']

print(sorted(fruits)) #sorted list
print(fruits) #original list

print(sorted(fruits,reverse=True))

print(fruits)