
# 1.Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
# (six hexadecimal numbers written after
# . Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet,a-f.
# Check the task 6 for output examples).

import string
import random
def list_of_hexa_colors():

    hexa_digits = string.hexdigits
    result = '#'
    max_length = 5

    for i in range(max_length):

        result += ''.join(random.choice(hexa_digits))

    return result



print(list_of_hexa_colors())