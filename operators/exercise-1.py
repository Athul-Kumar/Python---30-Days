
#  DAY - 3

# Q-1

age = 10
print(type(age))
# Q-2

height = 20.5
print(type(height))
#  Q-3

comp = 4j
print(type(comp))


#  Q-4

# base = int(input("Enter the base : "))
# height = int(input("Enter the height: "))
#
# area = (base * height) /2
#
# print(f"The area of the triangle is {area}")

#  Q-5

# side_1 = int(input("Enter side a : "))
# side_2 = int(input("Enter side b : "))
# side_3 = int(input("Enter side c : "))
#
# perimeter = side_1 + side_2 + side_3
#
# print(f"The perimeter of the triangle is {perimeter}")


#  Q-6

# length = int(input("Enter the length of the rectangle: "))
# width = int(input("Enter the width of the rectangle: "))
# area = length * width
# print(f"The area of the rectangle {area}")
#
# perimeter = 2 * (length + width)
# print(f"The perimeter of the rectangle is {perimeter}")

#  Q-7
# import math
# radius = int(input("Enter the radius of the circle: "))
# area = math.pi * (radius ** 2)
# print(f"The area of the circle is {area}")

#  Q-8

# find slope y = 2x-2

#  equation = y = mx + b

slope_1 = 2

#  Q-9

# m = (y2-y1 / x2-x1)

slope_2 = (10 - 2) / (6 - 2)
print(slope_2)

# Euclidean distance formula (d) = d = √[(x2– x1)2 + (y2– y1 )2]

import math

d = math.sqrt((6-2)**2 + (10-2)**2)
print(d)


#  Q-10

if slope_1 > slope_2:
    print("slope_1 is greater")

elif slope_1 < slope_2:
    print("slope_1 is smaller")

elif slope_1 == slope_2:
    print("slope_1 and slope_2 are equal")

else:
    print("invalid result")


#  Q-12

py = len("python")
dr = len("dragon")

print(py < dr)

#   Q-13

pyth = "python"
drag = "dragon"
if "on" in pyth and drag: print("True")
else: print("false")


# Q -14

sentence = "I hope this course is not full of jargon"

if "jargon" in sentence: print("True")
else: print("False")


#  Q-15

print("on" not in pyth and drag)


#  Q -16

text = len("python")

float_text = float(text)

str_text = str(text)
print(type(float_text))
print(type(str_text))


#  Q - 17

# num = int(input("Enter a number: "))
#
# if(num % 2 == 0): print("even number")
# else:print("odd number")

#  Q - 18

n = 2.7
print(type(n))

int_n = int(n)
print(type(int_n))

if (7 // 3) == int_n: print("true")
else:print("False")

#  Q-19

if '10' == 10: print("true")
else:print("false")

#  Q-20

if (float('9.8') == 10): print("True")
else: print("False")



#  Q-21

# hours = int(input("Enter the hours : "))
# rate = int(input("Enter the rate per hours: "))
#
# weekly_earning = hours * rate
# print(f"you're weekly earning is {weekly_earning}")

#  Q-22

years = int(input("Enter number of years you have lived: "))

seconds = years * 365 * 24 * 60 * 60

print(seconds)