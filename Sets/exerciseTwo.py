from exerciseOne import A, B

print(A)
print(B)

"""
                    Exercise level - 2
                    
"""

# Join A and B

# method - 1 --> using union
print(A.union(B))

# method -2 --> using update

A.update(B)
print(A)

# Find A intersection B

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print(A.intersection(B))

#3.Is A subset of B

print(A.issubset(B)) #True

# 4.Are A and B disjoint sets

print(A.isdisjoint(B)) #False

# 5.Join A with B and B with A

# A with B

print(A.union(B))

# B with A
print(B.union(A))


# 6.What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# A/B -->28, 27
# B/A --> 28,27

# A/B U B/A --> 28,27

# 7.Delete the sets completely

del A
del B
print(A)
print(B)