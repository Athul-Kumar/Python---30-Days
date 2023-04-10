
"""

                        Arithmetic Operations

Operator            Name                        Example

+                   Addition                    x + y
-                   Subtraction                  x - y
*                   Multiplication              x * y
/                   Division                    x / y
%                   Modulus                     x % y
**                  Exponentiation              x ** y
//                  Floor Division              x // y


"""

# Examples

#  integers

print('addition', 1 + 2)
print('subtraction', 2-1)
print('multiplication', 2 * 3)
print('Division', 6 / 2)
print('division', 7 / 3)
print('Divison without remainder', 7 // 2) # Gives quotient
print('modulus', 7 % 3) #gives remainder
print('expo', 2 ** 5)  #gives 2's power 5 times


# problem sets

# 1. area of circle

r = 10
area_of_circle = 3.14 * r ** 2
print(f"Area of the circle ==> {area_of_circle}")

# 2. Area of the rectangle

l = 10
w = 20
area_of_rectangle = l * w
print(f"Area of rectangle is {area_of_rectangle}")

# 3.weight of an object
mass = 75
g = 9.81
weight = mass * g
print(f"weight of an object --> {weight}")

# 4.Density of a liquid

m = 75
v = 0.075

D = m / v

print(f"Density of liquid is {D}")



"""
            Precedence of arithmetic operation
            
1.p --> parentheses
2.E --> Exponents
3.M  --> Multiplication
4.D ---> Division
5.A --> Addition
6.S ---> Subtraction

p>E>M>D>A>S ====> PEMDAS

"""

