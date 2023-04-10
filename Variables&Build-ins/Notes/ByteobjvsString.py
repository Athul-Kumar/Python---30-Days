
"""
                BYTE OBJECTS

1.Byte objects are sequence of byte
2.Byte objects are machine readable internally
3.Directly stored  on the disk (Encoding and Decoding not required)

"""

"""
                STRING OBJECTS
                
1.Strings are sequence of characters
2.String objects are Human readable form
3.Need to encode for storing on disk

"""


#  encoding --> converting string to byte objects

# initialising a String
a = "30 days of python series!"
# initialising a byte object
c = b'30 days of python series!'

# using encode() to encode the String
# encoded version of a is stored in d
# using ASCII mapping
d = a.encode('ASCII')
# checking if a is converted to bytes or not
if (d == c):
    print("Encoding is successful")
else:
    print("Encoding unsccessful")


print(type(d))
print(type(c))



# Decoding --> converting byte object to string

# initialising a String
a = "30 days of python series!"

# initialising a byte object
c = b'30 days of python series!'

# using decode() to decode the Byte object
# decoded version of c is stored in d
# using ASCII mapping
d = c.decode('ASCII')

# checking if c is converted to String or not
if (d == a):
    print("Decoding successful")
else:
    print("Decoding Unsuccessful")