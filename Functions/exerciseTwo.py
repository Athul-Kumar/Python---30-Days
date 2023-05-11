

# 1.Declare a function named evens_and_odds .
# It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(num):

    count_odd = 0
    count_even = 0

    for i in range(num + 1):
        if i % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f"The number of odds are {count_odd}.")
    print(f"The number of evens are {count_even}.")

evens_and_odds(num = 100)


# 2.Call your function factorial,
# it takes a whole number as a parameter and it return a factorial of the number


def factorial(num):
    total = 1
    for n in range(1, num+1, 1):
        print(n)
        total *= n
    return total

print(factorial(num = 7))


# 3.Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(num_list):

    if (len(num_list)) == 0:
        return 0

    else:
        return 1


num_list = []

if is_empty(num_list):

    print("this item is not empty")

else:
    print("this item is empty")



# 4.Write different functions which take lists. They should calculate
# _mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std
# (standard deviation).


def calculate_mean(number_list):

    total = 0
    for num in number_list:
        total += num

    count = len(number_list)
    mean = total / count
    return mean

def  calculate_median(number_list):

   length_of_list = len(number_list)
   middle_number = length_of_list // 2
   sum_of_numbs = number_list[middle_number - 1] + number_list[middle_number]
   count = 2
   median = sum_of_numbs / count
   return median


def calculate_mode(repeated_list):
    pass


def calculate_range():
    pass

def calculate_variance():
    pass

def calculate_std ():
    pass

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

repeated_list = [1,2,3,1,2,1,1,1,4,5,6]

print(calculate_mean(number_list))

print(calculate_median(number_list))

calculate_mode(repeated_list)

calculate_range()

calculate_variance()

calculate_std()