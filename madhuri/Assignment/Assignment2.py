"""
SQA Tools
Python Basic Programs
11 to 20
11)Formula : (a – b)2 = a^2 + b^2 – 2ab
12)Formula : a2 – b2 = (a-b)(a+b)
13)Formula : (a + b)3 = a3 + 3ab(a+b) + b3
14)Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
15). Python program to calculate the area of the square.
Formula : area = a*a
16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14
17). Python program to calculate the area of a cube.
Formula = 6*a*a
18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r
19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time
"""

"""
    11. Formula : (a – b)2 = a^2 + b^2 – 2ab
"""
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))

LHS = ( a - b ) ** 2
RHS = ( a** 2 ) + ( b ** 2 ) - 2 * a * b
print("11. LHS=RHS: ",LHS,'=',RHS)
print("_"*100)

"""
12. Formula : a2 – b2 = (a-b)(a+b)
"""
LHS_12 = ( a ** 2 ) - ( b ** 2 )
RHS_12 = ( a - b ) * ( a + b )
print("12. LHS=RHS: ",LHS_12,'=',RHS_12)
print("_"*100)

"""
13)Formula : (a + b)3 = a3 + 3ab(a+b) + b3
"""
LHS_13 = ( a + b ) ** 3
RHS_13 = (a ** 3) + 3 * a * b * ( a + b ) + (b ** 3)

print("13. LHS=RHS: ",LHS_13,'=',RHS_13)
print("_"*100)

"""
14)Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3
"""
LHS_14 = ( a - b ) ** 3
RHS_14 = ( a ** 3) - ( 3 * a * 2 * b) + (3 * a * b * 2 ) - (b ** 3)

print("14. LHS=RHS: ",LHS_14,'=',RHS_14)
print("_"*100)

"""
15.Python program to calculate the area of the square.
Formula : area = a*a
"""
side = float(input("Enter the side of square: "))
print("Area of square is: area = a*a ==> ",side ** side)
print("_"*100)

"""
16.Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14
"""
radius = float(input("Enter the radius of a circle: "))
PI = 3.14
print("Area of circle is: PI*r*r ==> ", PI * radius * radius)
print("_"*100)
"""
17. Python program to calculate the area of a cube.
Formula = 6*a*a
"""
side_cube = float(input("Enter the side of cube: "))
print("Area of cube is: 6*a*a ==>  ", 6* side_cube* side_cube)
print("_"*100)
"""
18: Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r
"""
radius_cyldr = float(input("Enter the radius of cylinder: "))
height_cyldr = float(input("Enter the height of cylinder: "))
area_cydr = 2* PI * radius_cyldr * height_cyldr + 2 * PI * radius_cyldr * radius_cyldr
print("Area of cylinder is ==> ", radius_cyldr )
print("_"*100)

"""
19.Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
"""
num = int(input("Enter a number: "))
sum = 0

temp = num
while temp > 0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp // 10

if num == sum:
    print(num, "Is Armstrong")
else:
    print(num, "Is not Armstrong")
print("_"*100)
"""
20). Python program to calculate simple interest.
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time
"""

p = 1000
r = 5
t = 2

amount = p + (p/r)*t
print(amount)
print("_"*100)