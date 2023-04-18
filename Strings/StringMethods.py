# Python strings as sequence of characters

# extracting single character from a string


'''  unpacking method'''

language = 'python'
a, b, c, d, e, f = language

print(a) #p
print(b) #y
print(c) #t
print(d) #h
print(e) #o
print(f) #n

#  Accessing characters in a string by index

language = 'Ruby on rails'
first_letter = language[0] #first letter
print(first_letter)
last_letter = language[-1]  # last letter
print(last_letter)

second_last = language[-2]
print(second_last)

#  slicing python string

tool = "continous integration"

first_three = tool[:3]
print(first_three)
last_three = tool[-4:]
print(last_three)

"""  different ways"""

first_three = tool[0:3]
print(first_three)
last_three = tool[17:21]
print(last_three)

''' Reversing a string '''

print(tool[::-1])

'''  skipping characters while slicing'''

#  skipping 2 characters

print(tool[0:21:2])



"""
                        STRING METHODS
                        
python methods for finding and using string methods

1. dir() --> print(dir(str)) ==> shows all the methods available for python string
2.help() --> print(help(string.method name)  ==> shows detailed info about that method
                        
"""
# capitalize() -->  Converts the first character of the string to capital letter

name = "athul kumar"
print(name.capitalize())

# count()  --> returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.

challenge = '30 days of python challenge'

print(challenge.count('a', 4, 21))
print(challenge.count('y'))


# endswith() --> Checks if a string ends with a specified ending

anime = 'Bungo stray dogs part two'

print(anime.endswith('two'))

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

domain = 'development\tand\toperations\t'

print(domain.expandtabs())

# find() --> Returns the index of the first occurrence of a substring, if not found returns -1

print(anime.find('o'))
print(anime.find('z'))

# rfind(): Returns the index of the last occurrence of a substring, if not found returns -1

print(anime.rfind('o'))
print(anime.rfind('z'))

# format(): formats string into a nicer output

first_name = "athul"
last_name = "kumar"

print('my name is {}, {}'.format(first_name,last_name))


# index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.


print(anime.index('y'))
# print(anime.index('z'))  ValueError: substring not found

# rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)

print(anime.rindex('p'))

# isalnum(): Checks alphanumeric character

name = "athul"

print(name.isalnum())
challenge = '30 days of python'
print(challenge.isalnum())  #space is not alphanumeric


# isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)

print(anime.isalpha())  #space is once again excluded
print(name.isalpha())

# isdecimal(): Checks if all characters in a string are decimal (0-9)

digits = '1234567890'
print(digits.isdecimal())
letters = 'abcdef'
print(letters.isdigit())

# isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name

print(name.isidentifier())

value ='90kdn'
print(value.isidentifier())


# islower(): Checks if all alphabet characters in the string are lowercase

print(name.islower())
print(anime.islower())

# isupper(): Checks if all alphabet characters in the string are uppercase

print(name.isupper())
first_name = "ATHUL"
print(first_name.isupper())


# join(): Returns a concatenated string

fruit_list = ['apple', 'mango', 'orange']

print(type(fruit_list))
fruits = ','.join(fruit_list)
print(fruits)
print(type(fruits))

# strip() --> Return a copy of the string with leading and trailing whitespace removed. , also Removes all given characters starting from the beginning and end of the string

word = '  30 days of python   '
print(word)
print(word.strip())

challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth'))
name = "athul kumar m u"
print(name.strip('alu'))

# replace(): Replaces substring with a given string

anime_name = 'The Vinland Sage Of Thorinn'
# replacing  V with W

print(anime_name.replace('V', 'W'))

# split(): Splits the string, using given string or space as a separator , change string to list

name = 'athul amar jithin ajmal'
print(type(name))

names = name.split()
print(type(names))

# title(): Returns a title cased string

movie = 'the untold story of dracula'

print(movie.title())

# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

print(movie.swapcase())

# startswith(): Checks if String Starts with the Specified String

print(movie.startswith('the'))
print(movie.startswith('story'))