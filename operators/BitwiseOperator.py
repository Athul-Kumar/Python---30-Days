
# Bitwise Operators --> act on bits and perform bit-by-bit operations.These are used to operate on binary numbers.


"""
Operator                        Description                     Syntax

&                           Bitwise AND                         x & y
|                           Bitwise OR                          x | y
~                           Bitwise NOT                         ~x
^                           Bitwise XOR                         x ^ y
>>                          Bitwise right shift                 x>>
<<                          Bitwise left shift                  x<<


"""


a = 10
b = 4

"""
a = 1010
b = 0100

"""

print(a & b) #  0000
print(a | b) #  1110  --> 14
print(a ^ b) #  1110  --> 14
print(~a)   #   -11
print(a >> 2) # a = 1010 --> after right shift by 2 place --> 0010 = 2
print(a << 2) # a = 1010 --> after left shift by2 place  -->  00101000 = 40
