var1 = 25
print(id(var1))

var2 =10
print(id(var2))

var3 =25
print(id)

# 1. Python Program to add two integer values.
A = 50
B = 20
print("Print two integer values",A,B)

# 2. Python Program to subtract two integer values
A=10
B=5
C=A-B
print("Subtraction:=",C)

# 3.Python program to multiply two numbers
A=10
B=5
C=A*B
print("Subtraction:=",C)

"""4). Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools” """

A="SQATools"
print("SQATools"*5)

"""5). Python program to get the Average of given numbers.
Formula: sum of all the number/ total number
Input:
a = 40
b = 50
c = 30
Output :
Average = 40"""

a = 40
b = 50
c = 30
print("Average of numbers",(a+b+c)/3)

"""6). Python program to get the median of given numbers.
Note: all the numbers should be arranged in ascending order
Formula : (n+1)/2
n = Number of values
Input : [45, 60, 61, 66, 70, 77, 80]
Output:  66"""
list1 = [45, 60, 61, 66, 70, 77, 80]
list1.sort()
a = (len(list1))/2
print("Median: ",list1[int(a)])

l1 = [1, 2, 3,4,7]
l1.sort()
n = len(l1) # length of the list
m = n // 2 # middle index
print("middle index", m)
# Check if the length is even or odd
if n % 2 == 0:
    res = (l1[m - 1] + l1[m]) / 2 # l1[3-1] + l1[3] = l1[2] + l1[3] = 7/2
    print(res)
else:
    res_1= (n + 1) / 2
    print(res_1)


"""7). Python program to print the square and cube of a given number.
Input :
num1 = 9
Output :
Square = 81
Cube =   729"""
a=9
print("square of num ", a**2)
print("cube of num ", a**3)

"""
8). Python program to interchange values between variables.
Input :
a = 10
b = 20
Output :
a = 20
b = 10"""

a = 10
b = 20
a,b = b,a
print("interchage values of a",a)
print("interchage values of b",b)

"""9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)"""
import math
a=40
b=50
c= (a**2+b**2)
print("answer is",math.sqrt(c))



"""10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab"""
a=5
b=6
print("answer is",(a+b)**2)

"""
11). Python program to solve the given math formula.
Formula : (a – b)2 = a^2 + b^2 – 2ab"""

a=5
b=6
print("answer is",(a-b)**2)

"""12). Python program to solve the given math formula.
Formula : a2 – b2 = (a-b)(a+b)"""
a=6
b=5
print("answer is",a**2 - b**2)

"""13). Python program to solve the given math formula.
Formula : (a + b)3 = a3 + 3ab(a+b) + b3 """
a=6
b=5
print("answer is",(a+b)**3)

"""14). Python program to solve the given math formula.
Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3"""
a=6
b=5
print("answer is",(a-b)**3)

"""15). Python program to calculate the area of the square.
Formula : area = a*a"""
a=10
print("area of square",a**2)


"""
16). Python program to calculate the area of a circle.
Formula = PI*r*r
r = radius
PI = 3.14"""
p=3.14
r=2
print("area of circle",p*r**2)

"""17). Python program to calculate the area of a cube.
Formula = 6*a*a"""

a=5
print("area of a cube",6*a**2)

"""18). Python program to calculate the area of the cylinder.
Formula = 2*PI*r*h + 2*PI*r*r"""
pi=3.14
r=3
h=5
print("area of the cylinder",2*pi*r*h + 2*pi*r*r)


"""19). Python program to check whether the given number is an Armstrong number or not.
Example: 153 = 1*1*1 + 5*5*5 + 3*3*3"""




#20). Python program to calculate simple interest.
p=1000
r=10
t=2
a=p+(p/r)*t
print("print simple interest 1",a)






