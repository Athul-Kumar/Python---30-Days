"""
                    Reverse words in a given String in Python
"""


# method-1

string = "geeks quiz practice code"
split_string = string.split(" ")
list_reversed = split_string[::-1]
str_reversed = " ".join(list_reversed)
print(str_reversed)



