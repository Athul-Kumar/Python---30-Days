
"""
                Find length of a string in python
"""

# method-1

string = "GeeksForGeeks"
print(len(string))

# method-2

count = 0
for i in string:
    count += 1
print(count)

# method-3

s = 0
for i, e in enumerate(string):
    s += 1
print(s)