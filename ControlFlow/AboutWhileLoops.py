"""
                                LOOPS

* In order to handle repetitive task programming language use loops.

* Python programming language follows two loops

    1.while loops
    2.for loops

1.while loops --> is used to execute a block of statements repeatedly until a given condition is satisfied.
                  And when the condition become false , the line immediately after the loop in the progra,
                  is executed.

syntax of while loop

while condition:
    code goes here

** In the above while loop, the condition becomes false when count is 5. That is when the loop stops.
If we are interested to run block of code once the condition is no longer true, we can use else.

syntax of while -else loop

while condition:
    code goes here

else:
    code goes here

break and continue in while loop

* break --> we use break when we like to get out of or stop the loop

syntax

while condition:
    code goes here

    if another_condition:
    break

* continue --> with continue statement we can skip the current iterationm, and continue with next.

syntax

while condition:
    code goes here

    if another_condition
        continue

2.For loops --> for loop is used for iterating over  a sequence
                (that is a list, tuple, dict, set, string)

*for looops with list

syntax
for iterator in list:
    code goes here


* for loop with string

syntax
for iterator in string:
    code goes here

* for loop with tuples

syntax
for iterator in tups:
    code goes here

* for loop with dictionary --> gives you key of dict

syntax
for iterator in dct:
    code goes here

* for loop with sets --> to access list item for loop is used

syntax

for iterator in set:
    code goes here

** for loop with break --> to break the iteration
syntax

for iterator in sequence:
    code goes here
    if condition:
        break

** for loop with continue --> to skip some of the steps in the iteration of the loop

syntax
for iterator in sequence:
    code goes here

    if condition:
        continue

$$ Range Function --> Range function return range of objects.
                     The range(start, end, step) takes three parameters: starting, ending and increment.
                      By default it starts from 0 and the increment is 1
                      The range sequence needs at least 1 argument (end)

syntax of range()

for iterator in range(start, stop, step):

** Nested for loop --> for loop inside another for loop

syntax
for x in y:
    for t in x:
        print(t)

**for-else :--> If we want to execute some message when the loop ends, we use else.

syntax

for iterator in range(start,end,step):
    do something

else:
    print('The loop ended')

**pass --> In python when statement is required (after semicolon),
            but we don't like to execute any code there, we can write the word pass to avoid errors.
            Also we can use it as a placeholder, for future statements.

syntax

for iterator in sequence:
    pass
"""


# example for while loop

count = 0

while count < 5:
    print(count)
    count += 1

# count while print 0,1,2,3,4
"""
In the above while loop, the condition becomes false when count is 5. That is when the loop stops. 
If we are interested to run block of code once the condition is no longer true, we can use else.
"""

# example for while else loop

count = 0

while count < 5:
    print(count)
    count += 1

else:
    print(count)

# The above loop condition will be false when count is 5 and the loop stops, and execution starts the else statement.
# As a result 5 will be printed.

# while with break

print("-------")
count = 0

while count < 5:
    print(count)

    count += 1
    if count ==3:
        break

# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.

# while loop with continue statement

print("////////////////")

# count = 0
# while count < 5:
#
#     if count == 2:
#         continue
#     print(count)
#     count += 1

# The above while loop only prints 0, 1, 2 and 4 (skips 3).


# For loops

# 1.for loops with list

numbers = [0, 1, 2, 3, 4, 5]

for number in numbers:  #number is temporary name to refer to the list's items, valid only inside this loop
    print(number) #the number will be printed line by line , from 0 to 5


# 2.for loop with string
print(";;;;;;;;;;;;;;;;;;;;;;;;;;;;;")
language = 'Python'

for lang in language:
    print(lang)

# method -2
for i in range(len(language)):

    print(language[i])

# for loop with tuple

print("----------------------")

numbers = (1,2,3,4,5)
for n in numbers:
    print(n)


# for loop with dict

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

for key in person:
    print(key)

# keys only

# method -2

for key, value in person.items():
    print(key, value)

# this way we get both keys and values printed out


# for loop with sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

for company in it_companies:
    print(company)


# for loop with break

numbers = (0, 1, 2, 3, 4, 5)

for num in numbers:
    if num == 4:
        break
    print(num)


# In the above example, the loop stops when it reaches 4.

# for loop with continue

numbers = (0, 1, 2, 3, 4, 5)
for num in numbers:
    if num == 4:
        continue
    print(num)




# range function examples

# 1. creating sequence of range of list

lst = list(range(11))
print(lst)

# 2.creating set

st = set(range(0,11,2))
print(st)

# iterating over range function

for number in range(11):
    print(number)


# nested loop example

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

for key in person:
    if key =='skills':
        for skill in person.get('skills'):
            print(skill)


# example for for-else

for number in range(11):
    print(number)

else:
    print('the loop stops at', number)

# example for pass

for number in range(6):
    pass