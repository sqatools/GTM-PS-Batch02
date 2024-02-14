#Python program to solve the given math formula.
#Formula : a2 – b2 = (a-b)(a+b)
a= 3
b= 2
Result = (a-b)*(a+b)
print("a^2-b^2:", Result)

#Python program to solve the given math formula.
#Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a=3
b=2
result= a**3+3*a*b*(a+b)+b**3
print("(a+b)^3:", result)

#Python program to solve the given math formula.
#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
a=3
b=2
result= a**3-3*a**2*b+3*a*b**2-b**3
print("(a-b)^3:", result)

print("_"*40)
#Python program to calculate the area of a circle.
'''
Formula = PI*r*r
r = radius
PI = 3.14
'''

r= int(input("enter radius value :"))
area= 3.14*r*r
print("Area of Circle", area)

# Python program to calculate the area of a cube.
# Formula = 6*a*a

a= int(input("enter side value :"))
area1= 6*a*a
print("Area of Cube", area1)


# Python program to calculate the area of the cylinder.
# Formula = 2*PI*r*h + 2*PI*r*r
radius= int(input("Enter radius of Cylinder :"))
height= int(input("Enter height of Cylinder :"))

area2= 2*3.14*radius*height + 2*3.14*radius*radius
print("Area of Cylinder :", area2)

#Python program to calculate simple interest.
'''
Formula = P+(P/r)*t
P = Principle Amount
r = Annual interest rate
t = time
'''
P= int(input("Enter Principle Amount :"))
r= int(input("Enter rate of interest :"))
t= int(input('Enter time :'))

SI= P+(P/r)*t
print("Simple Interest :", SI)


# Python program to solve this Pythagorous theorem.
#Theorem : (a2 + b2 = c2)
import math
a=5
b=4
hypo= a**2+b**2
print("Hypotenious side:", math.sqrt(hypo))