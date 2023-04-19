
"""
                Avoid Spaces in string length

"""

# method-1

test_str = "geeksforgeeks best"

# find length of string except space

new_str = test_str.replace(" ", '')
print(new_str)
print(len(new_str))

# method-2

test_str = "geeksforgeeks best"
count = 0

print("the original string is : " + str(new_str))

# result = sum(not t.isspace() for t in test_str)

for t in test_str:
    if not t.isspace():
        count += 1


print(f"The character avoiding spaces:  {count}")



