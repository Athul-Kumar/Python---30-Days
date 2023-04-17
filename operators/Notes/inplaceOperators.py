
"""
Inplace  operators behave similarly to normal operators except that they act in different manner
in case of mutable and immutable targets

normal operators add() method --> a+b and stores the result in the mentioned variable
implace operators add() method --> a+= b (not applicable for immutable objects)


The _add_ method, does simple addition, takes two arguments, returns the sum, and stores it in another variable without modifying any of the arguments.

On the other hand, _iadd_ method also takes two arguments, but it makes an in-place change in 1st argument passed by storing the sum in it. As object mutation
is needed in this process, immutable targets such as numbers, strings, and tuples, shouldn’t have _iadd_ method.
"""

# examples
#  immutable targets

import operator

x , y = 5, 6

a, b = 5, 6

z = operator.add(a, b)

print(z)

d = operator.iadd(x, y)
print(d)
print(a)
print(x)


# mutable

a = [1,2,3,4,5]

c = operator.add(a, [1,2,3])
print(c)

print(f"1st argument after normal operation{a}")

w = operator.iadd(a, [1,2,3])
print(w)
print(f"1st argument after inplace operation{a}")
