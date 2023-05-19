

# 1.Writ a function which generates a six digit/character random_user_id

import random
import string


def random_user_id():
    random_letters = string.ascii_letters + string.digits + string.punctuation
    max_length = 6
    result = ''

    for i in range(max_length):
        result += ''.join(random.choice(random_letters))
    return result

print(random_user_id())


# 2.Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.


# def user_id_gen_by_user(chars, ids):
#
#     random_letters = string.ascii_letters + string.punctuation + string.digits
#     result = ''
#     max_length = chars
#     nums_ids = ids
#
#
#     for i in range(nums_ids):
#         for j in range(max_length):
#
#             result += ''.join(random.choice(random_letters))
#
#     return result
#
# num_of_chars = int(input("Enter the number of characters for the password \n"))
# num_of_id = int(input("enter the number of ids for the password \n"))
#
# print(user_id_gen_by_user(chars = num_of_chars, ids = num_of_id))


# 3.Write a function named rgb_color_gen.
# It will generate rgb colors (3 values ranging from 0 to 255 each).


def rgb_color_gen():

    first_set = random.randint(100, 255)
    second_set = random.randint(100, 255)
    third_set = random.randint(100, 255)

    result = f'rgb({first_set},{second_set},{third_set})'

    return result


print(rgb_color_gen())