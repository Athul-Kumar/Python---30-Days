
#  Creating a String

letter = "P"
print(letter)  #P
print(len(letter)) #1
greeting = 'Hello, World!'
print(greeting)  #Hello, world!
print(len(greeting)) # 13
sentence = "I hope you are enjoying 30 days of Python challenge"
print(sentence) #I hope you are enjoying 30 days of Python challenge

# Multiline String

# 1.triple single quotes

multiline_string  = '''I am  a teacher and enjoying teaching.
I didn't find anything as rewarding ad empowering people.
That is why I created 30 days of python

'''

print(multiline_string)



#  2. triple double quotes (""")

multiline_string  = """I am  a teacher and enjoying teaching.
I didn't find anything as rewarding ad empowering people.
That is why I created 30 days of python"""

print(multiline_string)


#  String concatenation

first_name = "Athul"
last_name = "Kumar"
space = " "

full_name = first_name + space + last_name
print(full_name) # Athul Kumar

print(len(first_name))  #5
print(len(last_name))   #5
print(len(space))       #1
print(len(full_name))   #11
print(len(first_name) >= len(last_name))


#  Escape sequence in string

"""
In Python and other programming languages \ followed by a character is an escape sequence

* \n = newline
* \t = Tab means (4 spaces)
* \\ = Back slash
* \' = single quote (')
* \" = Double quote (")
"""

# use cases
print("I hope everyone is enjoying the Python Challenge.\nAre you?")  #line break
print('Days\tTopics\tExercise') #adding 4 spaces
print('Day1\t3\t5')
print('Day2\t3\t5')
print('This is the backslash symbol (\\)')
print('In every programming language starts with\"Hello, world!\"')

"""
                    OUTPUTS
                    
1.I hope everyone is enjoying the Python Challenge.
Are you?
2.Days  Topics  Exercise
3.Day1  3       5
4.Day2  3       5
5.This is the backslash symbol (\)
6.In every programming language starts with "Hello, world!"
"""


#  String formatting

"""
                    1.Old style of formatting string(% Operator)

* %s = String (or any object with a string representation, like numbers
* %d = Integers
* %f = Floating point numbers
* %.number of digitsf = Floating point numbers with fixed precision

                
"""

# Exercise

# Strings

first_name = "Athul"
last_name = "Kumar"
language  = "python"

formatted_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formatted_string)


#  string and number
radius = 10
pi = 3.14
area = pi * radius **2

formatted_string = 'The area of the circle with a radius %d is %.2f' %(radius,area)
print(formatted_string)


#  another example

Hero = "kiristu emiya"
villian = "Gilgamesh"
anime = "Fate-Zero Series"
power_range = 555.55

sentence = 'The hero %s killed the villian %s from a distance of %.3f by shooting in the anime %s'%(Hero,villian,power_range,anime)

print(sentence)



                        # 2.New style string formatting(str.format)


first_name = "Monkey"
middle_name = "D"
last_name   = "Luffy"
role = "captain"

full_name = 'I am {} {} {}. {} of this ship.'.format(first_name,middle_name,last_name,role)
print(full_name)
                        
#  exercise - 2

a = 6
b = 4

print('{} + {} = {}'.format(a, b, a+b))  # 6, 4 , 10
print('{} - {} = {}'.format(a,b, a-b))   # 6, 4,  2
print('{} * {} = {}'.format(a,b, a*b))   # 6, 4, 24
print('{} / {} = {}'.format(a,b, a / b)) # 6, 4, 1.5
print('{} % {} = {}'.format(a, b, a % b)) # 6, 4 , 2
print('{} // {} = {}'.format(a, b, a // b)) # 6, 4 , 1
print('{} ** {} = {}'.format(a, b, a**b))  # 6, 4, 1296



#  another example

num_1 = 10
num_2 = 20
sum = num_1 + num_2

print('sum of {2}, and {0} is {1}'.format(num_2,sum,num_1))



                    # f-string(string interpolation)
                    


name = "zorrow"
skill = "swordsman"
kills = 500
role = "vice captain"

character = f"His name is {name} with skillset of {skill} who killed more than {kills} with his sword and he is the {role} of captain Luffy"

print(character)