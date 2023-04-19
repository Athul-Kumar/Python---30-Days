
"""
                    remove i’th character from string in Python

"""

# method -1

string = "GeeksForGeeks"

# remove 6th character from string

new_str = ""
for i in range(len(string)):
    if i != 5:
        new_str = new_str + string[i]


print(f"new string after removing ith character: {new_str}")


#  method-2

string = "GeeksForGeeks"
new_str = string.replace("F", "")
print(new_str)

#  method -3

string = "GeeksForGeeks"

new_str = string[:5] + string[6:]
print(new_str)