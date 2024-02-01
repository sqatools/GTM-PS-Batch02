# Program to add two integer values
a = 2
b = 5
c = a + b
print("addition of two integer value is: ", c)

# Program to subtract two integer values
x = 200
y = 50
sub = x - y
print("suntraction of two integer value is: ", sub)

#program to multiply two numbers.

mul = a * b
print("Multiplication of two integer value is: ", mul)

#program to repeat a given string 5 times

str1 = "SQATools"
res = str1 * 5
print(res)

#program to get the Average of given numbers.
#Formula: sum of all the number/ total number

a = 40
b = 50
c = 30

Total = a + b + c
avg = Total // 3
print("Average of given numbers is: ", avg)

#program to print the square and cube of a given number.

num1 = 9
square_root = 9 ** 2
cube_root = 9 ** 3
print("Square root of 9 is: ", square_root)
print("cube root of 9 is: ", cube_root)

#program to interchange values between variables.

a = 10
b = 20
a, b = b, a
print(a, b)

#program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab


a = 2
b = 3
#LHS
LHS = (a + b)**2
print("LHS: ", LHS)

#RHS
RHS = (a**2) + (b**2) +(2 * a * b)
print("RHS: ", RHS)

#Formula : (a - b)2 = a^2 + b^2 - 2ab

a = 2
b = 3
#LHS
LHS = (a - b)**2
print("LHS: ", LHS)

#RHS
RHS = (a**2) + (b**2) - (2 * a * b)
print("RHS: ", RHS)

#Formula : a2 – b2 = (a-b)(a+b)

a = 2
b = 3
LHS = a**2 - b**2
print("LHS: ", LHS)

#RHS
RHS = (a-b) * (a+b)
print("RHS: ", RHS)

#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a = 2
b = 3
LHS = (a+b)**3
print("LHS: ", LHS)

#RHS
RHS = a**3 + (3*a*b) * (a+b) + b**3
print("RHS: ", RHS)

#program to calculate the area of the square.
#Formula : area = a*a

a= 2
area = a*a
print("area of the square is: ", area)

# program to calculate the area of a circle.
'''Formula = PI*r*r
r = radius
PI = 3.14'''

r = 2.5
PI = 3.14
res = PI * r * r
print("area of a circle is: ", res)