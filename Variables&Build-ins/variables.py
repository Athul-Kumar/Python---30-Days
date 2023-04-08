
# variables = used to store data in computer memory

"""
Variable naming rules

1.A variable name must start with a letter or the underscore character
2.A variable name cannot start with a number
3.A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
4.Variable names are case-sensitive (firstname, Firstname, FirstName and FIRSTNAME) are different variables)

"""

"""
# examples of valid variable names

1.firstname
2.lastname
3.age
4.country
5.city
6.first_name
7.last_name
8.capital_city
9._if #if you want to use reserved names as variable
10.year_2023
11.year2023
12.current_year_2023  # snake case naming
13.birth_year
14.num1
15.num2
16.firstName #camelcase
"""

"""
invalid variable names

first-name
first@name
first$name
1first_name
num-1
1num
"""

# variable declaration & assignment

full_name = "athul Kumar"

# examples of variables declaration and assigning

first_name = "Athul"
last_name = "kumar"
country = "India"
age = 25
skills = ['HTML', 'CSS', 'Bootstrap', 'Django', 'Postgres', 'python', 'Git']


#  Declaring  multiple variables in a line

first_name, last_name, age = "Athul", "kumar", 25

print(age)
print(first_name)
print(len(first_name))

#  gettign input from user using input() func

# first_name = input("Enter you\'re name: ")
# print(first_name)
# print(type(first_name))

#  Casting = converting one data type to another data type

first_name = "john"

list_of_letters = list(first_name)
print(list_of_letters)
print(type(list_of_letters))

digits = "100"

numbs = int(digits)
print(numbs)
print(type(numbs))


