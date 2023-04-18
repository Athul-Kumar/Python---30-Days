
#  Q -1

T = "Thirty"
D = "Days"
O = "Of"
P = "Python"
space = " "

result_string = T + space + D + space + O + space + P
print(result_string)

#  Q-2

C = "Coding"
F = "For"
A = "All"
space = " "

result = C + space + F + space + A

print(result)

#  Q-3 & Q-4

company = "Coding For All"
print(company)

#  Q-5

print(len(company))
#  Q-6

# print(company.upper())

#  Q-7

# print(company.lower())

#  Q-8

print(company.capitalize())
print(company.title())
print(company.swapcase())

#  Q-9

print(company[:6])

#  Q-10

print(company.index("Coding"))
print(company.find("Coding"))
print(company.startswith("Coding"))


# Q-11
# print(company)
# company = "python"
# print(company)
#  Q-12

word = "Python for Everyone"

print(word.replace("Everyone", "All"))


#  Q-13
print(company)
print(company.split(' '))

#  Q-14

print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

#  Q-15

print(company[0])
print(company.index("C"))

#  Q-16

print(company[-1])
#  Q-17

print(company[10])

# Q-18

name = "python for Everyone"
print(name[0:18:7])

#  Q-20
company = "coding for all"

print(company.index("c"))

#  Q-21

code = "coding for all"
code = code.title()
print(code.index("F"))

#  Q-22

print(code)
print(code.rfind("l"))

#  Q-23

print('You cannot end a sentence with because because because is a conjunction'.index("because"))
print('You cannot end a sentence with because because because is a conjunction'.find("because"))

# Q-24

print('You cannot end a sentence with because because because is a conjunction'.rfind("because"))

# Q-25
print('You cannot end a sentence with because because because is a conjunction'[31:54])

# Q-26
print('You cannot end a sentence with because because because is a conjunction'.index("because"))

#  Q-28

print('Coding For All'.startswith('Coding'))

#  Q-29
print('Coding For All'.endswith('coding'))

#  Q-30
print('   Coding For All      ' .strip(" "))

#  Q-31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

#  Q-32

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']

print('# '.join(libraries))

#  Q-33

print("I\nam\nenjoying\nthis\nchallenge\n")
print("I\njust\nwonder\nwhat\nis\nnext")

#  Q-34

print("Name\tAge\tCountry\tCity")
print("Athul\t250\tFinland\tHelsinki")

#  Q-35
r = 10
a = 3.14
t = 314

print(f"radius = {r}\narea= {a} * radius ** 2\nThe are of a circle with radius {r} is {t} meters square.")