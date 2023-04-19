"""
            Python program to check whether the string is Symmetrical or Palindrome

    * A string is said to be symmetrical if both the halves of the string are the same
    * a string is said to be a palindrome string if one half of the string is the reverse of the other half or
        if a string appears same when read forward or backward.

"""

# #  Method -1

string = input("Enter a string to check: ")
half = int(len(string)/2)
print(half)
first_part = string[:half]
second_part = string[half:]
print(first_part)
print(second_part)
# symmetry

if first_part == second_part:
    print("this word is symmetrical ")

else:
    print("this word is not symmetrical")

# palindrome

if string == string[::-1]:
    print("this word is palindrome")
else:
    print("this word is not palindrome")



#  palindrome method -2

string = "malayalam"
start = 0
mid = (len(string)-1) // 2
end = len(string)-1
flag = 0


while(start <= mid):

    if string[start] == string[end]:

        start += 1
        end -= 1

    else:
        flag = 1
        break;

if flag == 0: print(f"The string {string} is palindrome")
else:print(f"The string {string} is not palindrome")
