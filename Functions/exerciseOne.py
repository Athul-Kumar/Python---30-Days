"""
                        Exercise Level - 1

"""


# 1.Declare a function add_two_numbers. It takes two parameters and it returns a sum.


def add_two_numbers(num_1, num_2):
    sum = num_1 + num_2
    return sum


result = add_two_numbers(10, 20)
print(result)


# 2.Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radius, pi):
    area = pi * (radius ** 2)
    return area


result = area_of_circle(pi=3.14, radius=10)
print(result)

# 3.Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments.
# Check if all the list items are number types. If not do give a reasonable feedback.


def add_all_nums(*args):
    total = 0
    num_list = list(args)
    print(num_list)
    nums = []

    for i in range(len(num_list)):

        if type(i) == int:

            nums.append(num_list[i])
            print(nums)





print(add_all_nums(1, 2, '8', 3.14, 5, 6, 7))


