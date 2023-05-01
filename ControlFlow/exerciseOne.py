"""
Exercise level -1

"""

# 1.Iterate 0 to 10 using for loop, do the same using while loop.

# for loop

# 1 range()

for i in range(0,11,1):
    print(i)

# 2.normal method
lst = [0,1,2,3,4,5,6,7,8,9,10]

for l in lst:
    print(l)

# using while loop

count = 0

while count < 11:
    print(count)
    count += 1


# question-2 Iterate 10 to 0 using for loop, do the same using while loop.

# 1.for loop with range()
print("......................")
for i in range(11, -1,  -1):
    print(i)

# 2.for loop
print("***************")
lst = [0,1,2,3,4,5,6,7,8,9,10]

for l in lst[::-1]:
    print(l)


# question - 3 Write a loop that makes seven calls to print(), so we get on the output the following triangle:


# 3
for i in range(8):
    for j in range(i):
        print("#", end=" ")

    print("\n")


# 4.
print("!!!!!!!!!!!!!!!!!!!!!!")
for i in range(8):
    for j in range(8):
        print("#", end=" ")

    print("\n")

# 5.

for i in range(0,11,1):
    print(f"{i} * {i} = {i ** 2}")


# 6.Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.


lst=  ['Python', 'Numpy','Pandas','Django', 'Flask']

# method-1
for i in lst:
    print(i)

# method-2

print("^^^^^^^^^^^^^^^^^^^^^^")

for i in range(len(lst)):
    print(lst[i])

# 7.Use for loop to iterate from 0 to 100 and print only even numbers

for n in range(0,101,1):

    if n % 2 ==0:
        print(n)

# 8.Use for loop to iterate from 0 to 100 and print only odd numbers

for n in range(0,101,1):
    if n % 2 == 1:
        print(n)