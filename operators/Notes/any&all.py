"""
Any --> used for successive or.return true if any of item true .
It return false if empty or all are false
"""

# example

lis = [True,False,False,False]
print(any(lis))

list_2 = [False,False,False]
print(any(list_2))



"""
All --> returns true if all of the items are True. successive of AND
"""

# example

list_3 = [True,True,True,True]
print(all(list_3))
list_4 = [True,True,False,True]
print(all(list_4))