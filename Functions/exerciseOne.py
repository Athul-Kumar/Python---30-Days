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
    nums = []

    num_list = list(args)
    for i in range(len(num_list)):
        if type(num_list[i]) == int:
            print("all the list items are numbers")
            nums.append(num_list[i])
        else:
            print(f"{num_list[i]} is not a number")

    for num in nums:
        total += num
    return total

print(add_all_nums(1,2,3,'8',4,5))


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.


def convert_celsius_to_fahrenheit(celsius):
    F = (celsius * 9/5) + 32

    fahrenheit = (f"coverting {celsius} c to {F} fahrenheit")
    return fahrenheit

print(convert_celsius_to_fahrenheit(40))


# 5.Write a function called check-season, it takes a month parameter and returns the season:
# Autumn, Winter, Spring or Summer.

def check_season(month):
    result = " "
    print(type(month))
    season = ['spring', 'summer', 'fall', 'winter']
    match month.title():
        case 'January':
            result = (f"the {month} is part of season {season[1]}")
        case 'February':
            result = (f"the {month} is part of season {season[1]}")
        case 'March':
            result = (f"the {month} is part of season {season[2]}")
        case 'April':
            result = (f"the {month} is part of season {season[2]}")
        case 'May':
            result = (f"the {month} is part of season {season[2]}")
        case 'June':
            result = (f"the {month} is part of season {season[3]}")
        case 'July':
            result = (f"the {month} is part of season {season[3]}")
        case 'August':
            result = (f"the {month} is part of season {season[3]}")
        case 'September':
            result = (f"the {month} is part of season {season[0]}")
        case 'October':
            result = (f"the {month} is part of season {season[0]}")
        case 'November':
            result = (f"the {month} is part of season {season[0]}")
        case 'December':
            result = (f"the {month} is part of season {season[1]}")

    return result

print(check_season('may'))


# 6.Declare a function named print_list. It takes a list as a parameter
# and it prints out each element of the list.


def print_list(num_list):
    for num in num_list:
        print(num)

print_list(num_list = [1,2,3,4,5,6,7,8,9,10])


# 7.Declare a function named reverse_list. It takes an array as a
# parameter and it returns the reverse of the array (use loops).


def reverse_list(list_item):
    reversed = []
    for items in list_item[::-1]:
        reversed.append(items)


    return reversed
print(reverse_list(list_item = [1,2,3,4,5,6,7,8,9]))

# 8.Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items


def capitalize_list_items(fruits):
    new_list = []
    for fruit in fruits:

        fruit = fruit.capitalize()
        new_list.append(fruit)
    return new_list
print(capitalize_list_items(fruits = ['apple', 'orange', 'mango', 'pappaya']))


# 9.Declare a function named add_item. It takes a list and an item parameters.
# It returns a list with the item added at the end.

def add_item(food_staff, item):

    food_staff.append(item)

    return food_staff

print(add_item(food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'], item = "Meat"))


# 10.Declare a function named remove_item. It takes a list and an item parameters.
# It returns a list with the item removed from it.

def remove_item(food_staff,item):

    food_staff.pop(2)
    return food_staff

print(remove_item(food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'], item='Mango'))

# 11.Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.