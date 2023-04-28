"""

            Exercises: Level 2
"""

# question - 1  #grade to students

# user_grade = int(input("Enter your mark: "))
#
# if user_grade >= 80 and user_grade <= 100:
#     print("Grade is A")
# elif user_grade >= 70:
#     print("Grade is B")
#
# elif user_grade >= 60:
#     print("Grade is C")
# elif user_grade >= 50:
#     print("Grade is D")
# elif user_grade < 50:
#     print("Grade is F")
#
# else:
#     print("can't decide your grade")


# question-2 season check

# user_month = input("Enter the month: ")

# if user_month == "September" or user_month =="October" or user_month =="November":
#     print(" season is Autumn.")
#
# elif user_month == "December" or user_month == " January" or user_month == "February":
#     print("season is Winter")
#
# else:
#     print("Season is summer")

# method-2

# if user_month in ["September", "October", "November"]:
#     print(" season is Autumn.")
#
# elif user_month in ["December", "January", "February"]:
#     print("season is Winter")
#
# else:
#     print("summer")

# Question - 3

fruits = ['banana', 'orange', 'mango', 'lemon']
user_fruit = input("Enter a fruit name: ")

if user_fruit not in fruits:
    fruits.insert(1, user_fruit)
    print(fruits)
    print(len(fruits))

else:
    print('That fruit already exist in the list')