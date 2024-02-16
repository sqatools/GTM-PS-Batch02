"""
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

#Python program to solve the given math formula.
##Formula : (a – b)2 = a^2 + b^2 – 2ab

a=15
b=20

LHS=(a-b)**2
print(LHS)
RHS=((a)**2) + ((b)**2) - (2*a*b)
print(RHS)

if RHS==LHS:
    print ("LHS is equal to RHS'")
else:
    print('LHS is not equal to RHS')

##Formula : a2 – b2 = (a-b)(a+b)

a=11
b=11

LHS=((a)**2)-((b)**2)
print(LHS)
RHS=(a-b) *(a+b)
print(RHS)

if RHS==LHS:
    print ("LHS is equal to RHS'")
else:
    print('LHS is not equal to RHS')
#(a + b)3 = a3 + 3ab(a+b) + b3
a=1
b=11

LHS=((a+b)**3)
print(LHS)
RHS=((a)**3)+((b)**3)+(3*a*b*(a+b))
print(RHS)

if RHS==LHS:
    print ("LHS is equal to RHS")
else:
    print('LHS is not equal to RHS')
##Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a=15
b=10

LHS=((a-b)**3)
print(LHS)
RHS=((a)**3)-((b)**3)-(3*((a)**2)*b)+(3*a*((b)**2))
print(RHS)

if RHS==LHS:
    print ("LHS is equal to RHS")
else:
    print('LHS is not equal to RHS')

#Python program to calculate the area of the square.
##ormula : area = a*a

a=5
area = a*a
print(area)

#Python program to calculate the area of a cube.
#Formula = 6*a*a

cube_area=a*a*a
print(cube_area)

#Python program to calculate :
#area of a circle-Formula = PI*r*r
#area of the cylinder-Formula = 2*PI*r*h + 2*PI*r*r
radius=4
height=5
PI = 3.14

area_circle=PI*(radius**2)
area_of_cyclinder = (2*PI*radius*height) + (2*PI*radius*radius)
print(area_circle)
print(area_of_cyclinder)

#Python program to calculate simple interest.
#Formula = P+(P/r)*t
p=40
rate=5
time=5
simple_interest=(p*rate*time)/100
print("this is a simple interest value:",simple_interest)

#Python program to check whether the given number is an Armstrong number or not.
#Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
num = 153
num1 = num
length = len(str(num))
amst_num = 0

while num > 0:
    temp = num%10
    amst_num = amst_num + temp**length
    num = num//10

print("armstrong value :", amst_num)

if amst_num == num1:
    print(num1," is armstrong number")
else:
    print(num1,"is not an armstrong number")



