"""
                                Functions

1.Function without parameters and without return value

** A Function is a reusable block of code or programming statments designed to perform a certain
    task
** To define or declare python provides the def keyword.
** The function block of code is executed only if the function is called or invoked

Syntax of function

* when we make a function, we call it declaring a function
*Function can be declared with  or without parameters.

# declaring a function
def function_name():
    codes
    codes

* when we start using it, we call it calling or invoking the function.

# calling a function

function_name()


2.Function without parameters and with return value

* Function can also return values

* if a function does not have a return statement , the value of the function is None.

Syntax

def function_name():
    code
    return value

3.Function with parameters and return value

* In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set)
     as a parameter

    $$ single parameter function --> if our function takes a parameter we should call out function with an argument

syntax
# declaring a function

def function_name(parameter)
    code
    code
    return value

# calling the function

print(function_name(argument))

        $$ Function with two parameters --> A function may or may not have a parameter or parameters
                                             A function may also have two or more parameters.
                                             If our function takes parameters we should call it with arguments.


SYntax

#  declaring a function

def function_name(paramter_1, parameter_2):
    codes
    codes
    return value

# calling a function

print(function_name(argument1, argument2)


4.function with parameters and without return value

syntax

# declaring a function

def function_name(para1, para2):
    codes
    codes
    print(codes)

# calling a function

function_name(arg1,arg2) #this function doesn't return anything so its None



!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

* Passing Arguments with key and value

** If we pass Arguments with key and value , the order of the argument does not matter

syntax

# declaring a function

def function_name(para1, para2):

    codes
    codes
    return value

# calling a function

function_name(para1= 'john', para2= "Doe")

 # the order of arguments does not matter here

 ^^ Return any kind of data types from a function


** FUNCTION WITH DEFAULT PARAMETER

* Sometimes we pass default values to parameters, when we declare the function
* if we do not pass arguments when we call the function, their default value will be used

syntax
# declaring a function

def function_name(para = name):
    codes
    codes

# calling function

function_name() ---> default value will be used

function_name(arg) ---> arg will be used

*************************************************************************

1.*ARGS --> Arbitrary Number of Arguments

* If we do not know the number of arguments we pass to our function,
we can create a function which can take arbitrary number of arguments by adding * before the parameter name.

* Allow to pass multiple non-keyword arguments

* args will be packed using *

* args data type will be tuple

Syntax

# declaration

def function_name(*args):
    code
    code
    return value

# calling the function

print(function_name(para1, para2, para3,....))

2.**KWARGS --> Allow to pass multiple keyword arguments

* type of Kwargs --> dict
* Kwargs will be packed using *


syntax

# declaring function

def funct_name(**Kwargs):

    code
    code
    return value

# invoking the function

print(funct_name(key="value", key2="value2", key3="value3")

"""


# example of function without paramerters


""" declaring the function """
def generate_full_name():

    first_name = "Athul"
    last_name = "Kumar"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)

""" calling the function """

generate_full_name()

# another example

def add_two_numbers():
    num_one = 10
    num_two = 20
    total = num_one + num_two
    print(f"the totoal of two numbers is : {total}")


add_two_numbers()
print(add_two_numbers())
#this function doesn't return anything so return value = None

# Function without parameters and with return value

"""     declaring a function    """

def generate_full_name():

    first_name = "Athul"
    space = " "
    last_name = "Kumar"
    full_name = first_name + space + last_name
    return full_name

"""   invoking a  function  """

user_name = generate_full_name()
print(user_name)
# this function have a return value

# another example for function without parameters and with return type

def add_two_numbers():

    first_num = 100
    second_num = 25
    result = first_num + second_num
    return result

# calling the function

total = add_two_numbers()
print(total)

# function with parameters and return value

def greeting_func(name):
    message = name + ' ' + 'Welcome to the world of programming!'

    return message


print(greeting_func('Athul'))

# another example

def addition_of_nums(large_num):
    small_num = 10
    total = small_num + large_num
    print(type(total))
    return total

result  = addition_of_nums(100)
print(result)

# another example  --> area of the circle

def area_of_circle(radius):

    pi = 3.14

    area = pi * (radius **2)
    return area

print(area_of_circle(10))

# another example --> sum of numbers

def sum_of_numbers(n):
    total =0

    for i in range(n+1):
        total += i

    return total


print(sum_of_numbers(10))
print(sum_of_numbers(100))


# b.function with two parameter and return value

def generate_full_name(first_name, last_name):
    space = " "

    full_name = first_name + space + last_name
    return full_name

print(generate_full_name('Athul', 'Kumar'))

# another example

def sum_two_numbers(first_num, second_num):

    total = first_num + second_num

    return total

print(f"total of two numbers {sum_two_numbers(10,20)}")

# calculate age

def find_age_func(current_year, birth_year):

    current_age = current_year - birth_year
    return current_age

print(f"the age of this person: {find_age_func(2023, 1997)}")

# 4.function with parameters and without return value

def find_age_func(current_year, birth_age):

    current_age = current_year - birth_age

    print(current_age)


find_age_func(2023, 1990)

# function Argument with key value pair

# 1.function (argument with out key value)

def user_name_fun(first_name, last_name):

    full_name = first_name + " " + last_name

    return full_name

print(user_name_fun("Kumar", "Athul"))

# here the arguments we have to give it in a proper order for accurate result
print(user_name_fun("Athul", "kumar"))

# 2.function (argument with key and value)

def user_name(first_name, last_name):

    full_name = first_name + " " + last_name
    return full_name

print(user_name(last_name="Kumar", first_name="Athul"))  ## here order of argument doesn't care


"""
-------------------------Examples for functions with any kinf of return data types----------------------
"""

# 1.returning a string

def print_name(first_name):
    return first_name

print(print_name("Athul"))
print(type(print_name("Athul")))


# 2.Returning a number

def sum_of_two(num_1,num_2):

    sum = num_1 + num_2

    return sum

print(sum_of_two(num_2= 100, num_1= 50))
print(type(sum_of_two(num_2= 100, num_1= 50)))

# 3. returning a boolean

def is_even_num(num):

    if num % 2 ==0:
        print('Even')
        return True

    else:
        return False


print(is_even_num(15))
print(is_even_num(10))
print(type(is_even_num(10)))

# 4.returing list

def collect_even(num):

    even_list = []

    for i in range(num+1):
        if i % 2 == 0:
            even_list.append(i)
    return even_list


print(collect_even(100))
print(type(collect_even(100)))


# default parameter with function

# example one --> user full name

def user_name(first_name = "Athul", last_name = "Kumar"):

    full_name = first_name + " " + last_name
    return full_name

print(user_name()) #here default parameter worked
print(user_name("amar", "nath")) # here args worked


# example two --> age calculation

def user_age(birth_year = 1997, current_year = 2023):

    current_age = current_year - birth_year
    return current_age

print(user_age())
print(user_age(current_year=2023, birth_year=1990))


# *ARGS examples

# 1. printing name

# normal case

def name_fun(first_name, last_name):

    full_name = first_name + " " + last_name

    return full_name

print(name_fun("Athul", "Kumar"))
# print(name_fun("Athul", "kumar", "M U")) # here we can't pass third argument


# *Args function

def name_fun(*args):

    for arg in args:
        print(arg, end=" ")


name_fun("Athul", "kumar", "M U")


# another example --> sum of all numbers

print("\n")
def sum_all_nums(*args):

    total =0
    for arg in args:

        total +=arg

    return total


print(sum_all_nums(1,2,3,4))
print(sum_all_nums(1))
print(sum_all_nums(1,2,3))

# **KWARGS Function

# normal keyword function

def full_name(first_name, last_name):
    full_name = first_name + " " + last_name

    return full_name

print(full_name(last_name="Kumar", first_name="Athul"))
# print(full_name(last_name="Kumar", first_name="Athul", nick_name ="athul")) # error

# **KWARGS

def full_name(**kwargs):
    print(type(kwargs)) #dict type

    for value in kwargs.values():
        print(value)

full_name(first_name ="Athul",
                middle_name="Kumar",
                last_name="M U")

#  exercise --> shipping label

def shipping_label(*args, **kwargs):

    for arg in args:
        print(arg, end=" ")

    print()

    for value in kwargs.values():
        print(value, end=" ")


shipping_label("Dr.", "Spongebob", "Squarepants", "III",
               street= "123 Fake",
               apartment="100",
               city="Detro",
               state="kerala",
               zip="54321")

"""    Default with args"""


def anime_info(odd, *args):
    print(odd) # naruto default

    for arg in args:
        print(arg)  #rest



anime_info("Naruto", "sasuke", "Itachi", "hidan", "Dedara")

