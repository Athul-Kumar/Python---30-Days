

"""
                    LOGICAL OPERATORS

operator            About                         Syntax

and         True:if both operands are true          x and y

or          True: if either of the operands true    x or y

not         True: if operand is false                not x


"""


# examples

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 < 2 and 4 < 3) #False
print('True and True: ', True and False) # False
print(3 > 2 or 4 > 3) # True
print(3 > 2 or 4 < 3) # True
print(3 < 2 or 4 < 3) # False
print('True or False: ', True or False) # True
print(not 3 > 2) # False
print(not True) # False
print(not False) # True
print(not not False) #False
print(not not True) #True