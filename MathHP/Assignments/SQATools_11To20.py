############################   Assignment 2 SQA Tools
import math

######################  11)Python program to solve the given math formula.
####### Formula : (a – b)2 = a^2 + b^2 – 2ab

a = 4
b = 3
result = a**2+b**2-2*a*b
print("(a-b)^2 : ", result)

##################### 12)Python program to solve the given math formula.
###### Formula : a2 – b2 = (a-b)(a+b)

p = 6
q = 4
result1 = (p+q)*(p-q)                                      # (p+q)*(p-q) * is essential orelse typo error
print("(p^2 - q^2):",result1)

#  result1 = (p+q)(p-q)
#               ^^^^^^^^^^
# TypeError: 'int' object is not callable

##################### 13)Python program to solve the given math formula.
#### Formula : (a + b)3 = a3 + 3ab(a+b) + b3

x = 3
y = 2
result2 = (x**3)+(3*x**2*y)+(3*x*y**2)+(y**3)
print("(x+y)^3 : " ,result2)

#################### 14) Python program to solve the given math formula.
#### Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

r = 9
s = 5
result3 = (r**3)-(3*r**2*s)+(3*r*s**2)-(s**3)
print("(r-s)^3 : ",result3)

################### 15)Python program to calculate the area of the square.
#### Formula : area = a*a

a = 10
area = a**2
print("Area of the square : " ,area)

################## 16) Python program to calculate the area of a circle.
# Formula = PI*r*r
# r = radius
# PI = 3.14

radius = 4
math.pi = 3.14
AreaOfTheCircle = math.pi*radius**2
print("Area of the Circle : ",AreaOfTheCircle)

################## 17)Python program to calculate the area of a cube.
### Formula = 6*a*a

side = 8
AreaOfTheCube = 6*side**2
print("Area of the Cube : ",AreaOfTheCube)

################## 18)Python program to calculate the surface area of the cylinder.
### Formula = 2*PI*r*h + 2*PI*r*r
### 2*pi*r(h+r)

r = 2
h = 3
#math.pi = 3.14
SurfaceAreaOfTheCylinder = (2*math.pi*r)*(h+r)
print("Surface area of the Cylinder : ", SurfaceAreaOfTheCylinder)

################### 19)Python program to check whether the given number is an Armstrong number or not.
### Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

##### In general, for a number with n digits, if the sum of the nth power of each digit equals the number itself, then it is an Armstrong number.

num = 153
num1 = num
arms_num = 0
reverse = 0
length = len(str(num))
                                                                          #print("Length of given number :" ,length)

while num>0:
 temp = num%10                      #3
                                                                        #reverse = reverse*10 + temp         # reverse = 3
 arms_num = arms_num + temp ** length
 num = num//10                    # ignores 3

                                                                       #print("Reverse number is :", reverse)
if arms_num == num1:
    print("The given number is Armstrong number :", num1)
else:
    print("The given number is not Armstrong number : ",num1)

################## 20)Python program to calculate the Amount in simple interest.
# Amount  = P+(P*n*r)
# P = Principal Amount
# r = Annual interest rate
# t = time = n ... Number of years

### This formula calculates the total amount of money (including both the principal and the interest) after a certain period of time under simple interest

P = 6000
N = 4
R = 10
Amount = P+(P*N*R)
print("Total Amount Calculated: ",Amount)




