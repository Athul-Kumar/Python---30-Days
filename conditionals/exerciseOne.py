"""
    Exercise Level - 1


"""

# question -1

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print(" You are old enough to drive")
else:
    print("to wait for the missing amount of years")

# method-2 (Ternary)

print(" You are old enough to drive") if user_age >= 18 else  print("to wait for the missing amount of years")

# Question -2

my_age = 25
year = user_age - my_age

if user_age > my_age:
    if year:
        print(f"You are {year} years older than me")

else:
    print("I'am older than you!")


# Question -3

a = int(input("Enter the first number: "))
b = int(input(("Enter the second number: ")))


if a > b:
    print("a is greater than b")

elif a < b:
    print("a is smaller than b")

else:
    print("a is equal to b")