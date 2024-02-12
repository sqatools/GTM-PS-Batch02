#1. Python Program to add two integer values
x = 50
y = 60

print("Add =",(x+y))

print('*'*60)

#2. Python Program to subtract two integer values

x = 1000
y = 670

print("Sub =",(x-y))

print('*'*60)


#3.Python program to multiply two numbers

X = 25
y = 4

print("Mul =",(X*y))

print('*'*60)


#4.Python program to repeat a given string 5 times.

str1 = "SQATools"

print(str1*5)

print('*'*60)

#5.Python program to get the Average of given numbers

a = 40
b = 50
c = 30

print("Average =",(a+b+c)//3)
print('*'*60)

#6.Program to get the median of given numbers.

list1 = [34,76,23,54,89,21,45]
Sort1 = sorted(list1)
print(Sort1)
n = len(Sort1)
median1 = ((n+1)/2)
print("Median =",median1)

print('*'*60)

#7.Python program to print the square and cube of a given number.
num1 = 9

print("Square =",num1**2)
print("Cube =",num1**3)
print('*'*60)

print('*'*60)


#8. Python program to interchange values between variables.

a = 10
b = 20

a,b = b,a
print("a =",a)
print("b =",b)
print('*'*60)

#9.Python program to solve this Pythagorous theorem.

from math import sqrt

a = 5
b = 8

c = sqrt(a**2+b**2)
print("pythagorous of c =",c)

print('*'*60)
#10.Python program to solve the given math formula.
#(a + b)2 = a^2 + b^2 + 2ab


a = 5
b = 7



print("(a+b)2 =",a**2+b**2+2*a*b)

print('*'*60)


#11.Python program to solve the given math formula.
#(a – b)2 = a^2 + b^2 – 2ab

a = 20
b = 4

print("(a-b)2 =",a**2+b**2-2*a*b)

print('*'*60)


#12. Python program to solve the given math formula
#a2 – b2 = (a-b)(a+b)

a = 50
b = 20

c = (a-b)*(a+b)

print("a2-b2=",c)
print('*'*60)


#13.Python program to solve the given math formula
#(a + b)3 = a3 + 3ab(a+b) + b3

a = 5
b = 6
c = a**3+3*a*b*(a+b)+b**3

print("(a+b)3=",c)
print('*'*60)


#14.Python program to solve the given math formula
#(a – b)3 = a3 – 3a2b + 3ab2 – b3

a = 8
b = 6

c = a**3-3*a**2*b+3*a*b**2-b**3

print("(a-b)3=",c)
print('*'*60)

#15.Python program to calculate the area of the square
#Formula : area = a*a

a= 12
area = a*a

print("area =",area )
print('*'*60)

#16.Python program to calculate the area of a circle.
"""Formula = PI*r*r
Formula = PI*r*r
r = radius
PI = 3.14"""

r = 4.6
pi = 3.14
area = pi*r*r
print("area of circle = ",area)
print('*'*60)


#17. Python program to calculate the area of a cube.
#Formula = 6*a*a

a = 7
area = 6*a*a

print("area of cube =",area)
print('*'*60)


#18.Python program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

pi = 3.14
r = 5
h = 8

area = 2*pi*r*h + 2*pi*r*r

print("area of cylinder =",area)
print('*'*60)

#20). Python program to calculate simple interest.
#Formula = P+(P/r)*t

p = 10000
r = 6
t = 2

SI = p +(p/r)*t

print("Simple Interest =",SI)
print('*'*60)


#21). Python program to print the current date in the given format

import datetime
Date = datetime.datetime.now()
print ("Date :",Date)
print('*'*60)

#22).Python program to calculate days between 2 dates.

from datetime import date

Date_1 = date(2023,1,25)
Date_2 = date(2024,2,1)
Day1 = (Date_2 - Date_1)
print(Day1.days)
print('*'*60)

#27). Python program to calculate compound interest

p = 15000
r = 6
n = 3

Inter = p*((1+r/100)**n)
print('Compound Interest =',Inter)
print('*'*60)

#33). Python program to get the current date.

import datetime

date1 = datetime.datetime.now()
print('Current date :',date1)

#38). Python program to find the square root of a number.

from math import sqrt

a = 144
b = sqrt(a)
print("square root of a :",b)











