#1. Python Program to add two integer values
x = 50
y = 60

print("Add =",(x+y))

#2. Python Program to subtract two integer values

x = 1000
y = 670

print("Sub =",(x-y))

#3.Python program to multiply two numbers

X = 25
y = 4

print("Mul =",(X*y))

#4.Python program to repeat a given string 5 times.

str1 = "SQATools"

print(str1*5)

#5.Python program to get the Average of given numbers

a = 40
b = 50
c = 30

print("Average =",(a+b+c)//3)

#7.Python program to print the square and cube of a given number.
num1 = 9

print("Square =",num1**2)
print("Cube =",num1**3)

#8. Python program to interchange values between variables.

a = 10
b = 20

a,b = b,a
print("a =",a)
print("b =",b)

#10.Python program to solve the given math formula.
#(a + b)2 = a^2 + b^2 + 2ab

a = 5
b = 7

print("(a+b)2 =",a**2+b**2+2*a*b)

#11.Python program to solve the given math formula.
#(a – b)2 = a^2 + b^2 – 2ab

a = 20
b = 4

print("(a-b)2 =",a**2+b**2-2*a*b)

#12. Python program to solve the given math formula
#a2 – b2 = (a-b)(a+b)

a = 50
b = 20

c = (a-b)*(a+b)

print("a2-b2=",c)

#13.Python program to solve the given math formula
#(a + b)3 = a3 + 3ab(a+b) + b3

a = 5
b = 6
c = a**3+3*a*b*(a+b)+b**3

print("(a+b)3=",c)

#14.Python program to solve the given math formula
#(a – b)3 = a3 – 3a2b + 3ab2 – b3

a = 8
b = 6

c = a**3-3*a**2*b+3*a*b**2-b**3

print("(a-b)3=",c)

#15.Python program to calculate the area of the square
#Formula : area = a*a

a= 12
area = a*a

print("area =",area )

#16.Python program to calculate the area of a circle.
"""Formula = PI*r*r
Formula = PI*r*r
r = radius
PI = 3.14"""

r = 4.6
pi = 3.14
area = pi*r*r
print("area of circle = ",area)

#17. Python program to calculate the area of a cube.
#Formula = 6*a*a

a = 7
area = 6*a*a

print("area of cube =",area)

#18.Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

pi = 3.14
r = 5
h = 8

area = 2*pi*r*h + 2*pi*r*r

print("area of cylinder =",area)

#20). Python program to calculate simple interest.
#Formula = P+(P/r)*t

p = 10000
r = 6
t = 2

SI = p +(p/r)*t

print("Simple Interest =",SI)

#21). Python program to print the current date in the given format

import datetime
Date = datetime.datetime.now()
print ("Date :",Date)



