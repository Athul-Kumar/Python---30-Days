
# python official documentation link for Build-in functions ---> https://docs.python.org/3/library/functions.html


#  commonly used build-ins in python

# 1. len() = counts number of characters including the space
text = "Hello,World!"
print(len(text))

# 2. type() = it checks the data type

print(type(text))

num = 10
print(type(num))

# 3. datatype conversion build-ins

# a. int() --> converts to number (string should be base to 10 fot converting to int)

digit = '10'

nums = int(digit)
print(type(nums))

# b. float() --> converts to floating point numbers (string should be base to 10 fot converting to float)

digit = '13.33'
print(type(digit))

nums = float(digit)
print(nums)
print(type(nums))

# c. str() = converts to string data type from other data types

num = 100

print(type(num))

digit = str(num)
print(digit + "100")
print(type(digit))

# d.list() --> creates list objects
# e. tuple() --> creates tuple objects
# f. set() --> creates set objects
# g. dict()--> creates dictonary objects

# 4. input() --> takes input from the user

# name = input("Enter you\'re name here: ")
# by default takes str data type

# 5. help() --> prints all python reserved words

print(help('keywords'))
# print(help('from'))
# print(help('if')) #gives the detailed info about the keyword

# 6. dir() --> which returns list of the attributes and methods of any object

# print(dir(str))

#  shows list of all the methods can be used with string

# 7.min() --> will finds the smallest number in the expression

print(dir(min)) #shows all the methods can be used in min
print(help(min))  # show all the detail info of how min() is used


#  etc the list goes on .......
