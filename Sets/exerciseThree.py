from exerciseOne import age

print(age)

"""
                        Exercise level- 3
"""

# 1.Convert the ages to a set and compare the length of the list and the set, which one is bigger?

ages = set(age)
print(age)

print(len(age)) #list --> 8
print(len(ages)) #set --> 5

# 2.Explain the difference between the following data types: string, list, tuple and set

"""
1.string --> immutable set of characters 
2.list --> ordered, indexed , mutable and allow duplicate
3.tuple --> ordered, immutable , allow duplicate and indexed
4.set --> unordered, unidexed, doesn't allow duplicates, mutable


"""

# 3. "I am a teacher and I love to inspire and teach people". How many unique words have been used in the sentence?
# Use the split methods and set to get the unique words.


words = "I am a teacher and I love to inspire and teach people"
words= words.split(' ')
unique_words = set(words)
print(unique_words)
print(len(unique_words))

