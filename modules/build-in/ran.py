"""
                            Random Module

---> random module will generate random values

if
--> 1.integers ==> uniform selection from a range

---> 2.sequences ==> uniform selection of a random elements

---> 3. function ==> generate a random permutation of a list in-place

"""

import random

print(random.random())
print(random.randint(1,10))
print(random.randrange(10))

li = [1,2,3,4,5]
random.shuffle(li)
print(li)