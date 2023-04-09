
"""
we can pass any number of args to function usinf packing and unpacking

"""

# packing


def sumOf(*args):
    print(type(args))
    num_1 = args[0][0]
    num_2 = args[0][1]
    num_3 = args[0][2]
    num_4 = args[0][3]
    sum_of_nums = num_1 + num_2 + num_3 + num_4
    return sum_of_nums

my_n = [5,20,50,70]

total = sumOf(my_n)
print(total)
print(type(my_n))

"""
In the function definition def sumOf(*args) we packed all the parameters in to one unit 
and its datatype is tuple
"""

# unpacking

def productOf(a,b,c,d):
    print(type(my_nums))
    a = my_nums[0]
    b = my_nums[1]
    c = my_nums[2]
    d = my_nums[3]
    product = a * b * c * d
    return product
my_nums = [10,50,60,100]
mutiple = productOf(*my_nums)
print(mutiple)
print(type(my_nums))

#  the main difference in packing and unpacking is when we pack --> the functional args will be in a tuple
# while unpack the funcitonsl args have to be definite in number and the parameters should pack in unpacking(it can be any data type list,tuple etc)