"""
        exercise level-2

"""

# question-1 Use for loop to iterate from 0 to 100 and print the sum of all numbers.
print(".................")
sum =0
for n in range(0, 101,1):

    sum += n
print(f"the sum of all numbers is {sum}")

# Q-2 Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.

print("=========================")

odd_sum = 0
even_sum = 0

for num in range(0,101,1):
    if num % 2 ==0:
        even_sum += num

    else:
        odd_sum += num


print(f"The sum of all even is {even_sum}. And the sum of all odds is {odd_sum}")