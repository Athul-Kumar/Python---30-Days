
# Sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


"""
                LEVEL - 1
"""

# 1.Find the length of the set it_companies

print(len(it_companies)) # 7

# 2.Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)


# Insert multiple IT companies at once to the set it_companies

it_companies.update(['Netflix', 'Tcs', 'wipro', 'Atlassin'])
print(it_companies)

# 4.Remove one of the companies from the set it_companies

# method-1 --> pop()
print(it_companies.pop())

# method -2 --> remove()

# it_companies.remove('Netflix')
# print(it_companies)
# # methof-3 --> discard()
#
# it_companies.discard('Oracle')
# print(it_companies)

# 5.What is the difference between remove and discard

"""
remove --> raises key error if the value is not present

discard --> error won't be raised if the value is not present
"""