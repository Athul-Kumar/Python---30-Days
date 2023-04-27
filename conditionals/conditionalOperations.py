
"""
1.if Condition -->  the key word 'if' is used to check if a condition is true and to execute the block code.


syntax

if condition:
    this part of code runs for truthy conditions

2.if - Else Condition --> If condition is true the first block will be executed,
                          if not the else condition will run.

syntax

if condition:
    this part of code runs for truthy condition
else:
    this part of code runs for false conditions

3.if - Elif - Else --> TO check more than 2 conditions in a simple way

syntax

if condition:
    code
elif condition:
    code
else:
    code

4.Ternary Operator --> short hand of if-else

syntax

code if condition else code

[on_true] if [expression] else [on_false]

5.switch case (match case in python) --> replacement for if - elif -else (only work with string data type)

syntax

match term:
    case pattern-1:
         action-1
    case pattern-2:
         action-2
    case pattern-3:
         action-3
    case _:
        action-default

6.Nested Conditions --> conditions that are nested

syntax

if condition:
    code

    if condition:
        code


7. if condition and logical operator

a.if - and operation
syntax

if condition and condition:
    code
b.if - or operation

syntax

if condition or condition:
    code

c.if - not operation  -> it reverses the condtion (if it true then it became false)

syntax

if not condition:
    code
"""

# example for if condition

a = 3

if a > 0:
    print("A is a positive Number")

"""
A is a positive number (True)
"""

# example for if - else

# a = int(input("Enter a number: "))

if a > 0:
    print('A is positive number')

else:
    print('A is a negative number')

# example of if-elif-else

# a = int(input("Enter a number: "))

if a > 0:
    print("A is a positive number")

elif a < 0:
    print("A is a negative number")

else:
    print("A is zero")


# Ternary operator

# a = int(input("Enter a number: "))

print("A is positive number") if a > 0 else print("A is a negative number")


# switch case in python

# example-1

# day = input("Enter a day from the day: ")

# match day.title():
#     case "Monday":
#         print("This is monday")
#
#     case "Tuesday":
#         print("This is tuesday")
#
#     case "Wednesday":
#         print("This is wednesday")
#
#     case "Thursday":
#         print("This is Thursday")
#
#     case "Friday":
#         print("This is Friday")
#
#     case "Saturday":
#         print("This is Saturday")
#
#     case "Sunday":
#         print("This is sunday")
#
#     case _:
#         print("You chosen wrong day")

#  Nested conditions

a = int(input("Enter a number: "))

if a > 0:

    if a % 2 ==0:
        print('A is positive and even number')

    else:

        print('A is positive and odd number')

elif a < 0:
    print('A is negative number')

else:
    print('A is zero')



# 7. if condition and logical operator

# a.if - and operation

numb_1 = 10
num_2 = 20

if numb_1 > 0 and num_2 > 0:

    result = numb_1 + num_2
    print(result)

else:
    print("false")


# b..if - or operation

password = "random123"
userName = "unknown"

if len(password) > 5 or len(userName) > 10:
    print("Access granded")

else:
    print("You can't enter")


# c.if -not operation

number_of_students = 50

if not number_of_students >= 50:
    print(" you can't go to tour")

else:
    print(f"the number of students {number_of_students}, you can go for tour")

