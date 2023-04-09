
"""

Global variables => which are not defined inside any function and have a global scope
local variables => which are defined inside a function and their scope is limited to that function only

"""

# local variables

def fun():

    tv_show = "Hell paradise"

    print(f"currently watching {tv_show}")


fun()


"""
#  accesing tv_show outside the function
print(tv_show)
"""

# Global variables

def fun():
    print(f"currently watching {show}")


show = "Bungko stray dog"
# scope of show is outside functional scope

fun()



"""
Global keyword => used to create a global variable from a non-global scope.

"""

def f():

# using without global keyword

    S = "Me too"
    print(S)


S = "I love watching anime"

f()
print(S)
# result --> Me too
# I love watching animeMe too
# I love watching anime


def f():
    global S

    S += "Hell paradise"
    print(S)


S = "I Love watching anime "

f()
print(S)

#  result --> I Love watching anime Hell paradise