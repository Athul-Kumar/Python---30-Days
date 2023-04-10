
# Assignment operators used to assign values to variables.

"""
            EXAMPLES

1. =    --> x = 5
2. +=   -->  x = x + 5
3. -=   --> x = x -5
4. /=   -->  x = x / 5
5. *=   --> x = x * 5
6. %=  --> x = x % 5
7. //=  ---> x = x // 5
8. **=   ---> x = x** 5
9. &=    --> x = x & 5
10.|=    --> x = x | 5
11. ^=   --> x = x ^ 5
12. >>=  ---> x = x >> 5
13. <<=  --->  x = x << 5

"""

#  Bitwise AND and Assign operation

a = 1
b = 1

a &= b

print(a)
print(b)

# bitwise AND = sets each bits to 1 if both are 1


# Bitwise OR and assign

# Bitwise OR --> sets each bits to 1 if one of them is 1

a = 3
b = 5

a |= b
print(a)
print(b)

# Bitwise XOR and Assign operation
# Bitwise XOR --> sets each bits to 1 if only one of two bits is 1

a = 3
b = 5
a ^= b

print(a)
print(b)

# Bitwise right shift and assign
# Bitwise right shift ---> 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

a = 3
b = 5

a >>= b
print(a)
print(b)

# Bitwise Left shift and assign
# Bitwise left shift --> Shift left by pushing zeros in from the right and let the leftmost bits fall off

a = 3
b = 5
a <<= b
print(a)
print(b)