"""
SQA Tools 
Python Basic Programs
1 to 10
1). Python Program to add two integer values.
2). Python Program to subtract two integer values.
3). Python program to multiply two numbers.
4) Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
5)Python program to get the Average of given numbers.
6). Python program to get the median of given numbers.
7). Python program to print the square and cube of a given number.
8). Python program to interchange values between variables.
9). Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)
10). Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab
"""

"""
 1. Python Program to add two integer values.
"""

num1 = int(input("Enter First Integer Number to Add: "))
num2 = int(input("Enter Second Integer Number to Add: "))

addition = num1 + num2
print("Addition of to integer number is: ",addition)
print("_"*100)
"""
2.Python Program to subtract two integer values.
"""

num3 = int(input("Enter First Integer Number to Subtract: "))
num4 = int(input("Enter Second Integer Number to Subtract: "))

subtraction = num3 - num4;
print("Subtraction of two integer number is: ",subtraction)
print("_"*100)

"""
3. Python program to multiply two numbers.
"""

num5 = int(input("Enter First Integer Number to Multiply: "))
num6 = int(input("Enter Second Integer Number to Multiply: "))

multiply = num5 * num6
print("Multiplication of two integer number is: ",multiply)
print("_"*100)

"""
5. Python program to repeat a given string 5 times.
Input :
str1 = “SQATools”
Output :
“SQAToolsSQAToolsSQAToolsSQAToolsSQATools”
"""
str1 = "SQATools"
print(str1*5)
print("_"*100)

"""
6.Python program to get the median of given numbers.
"""

"""
7.Python program to print the square and cube of a given number.
"""

num7 = int(input("Enter integer number to get square and cube of the given number: "))
print("Square of num: ",num7**2)
print("Cube of num: ",num7**3)
print("_"*100)

"""
8.Python program to interchange values between variables.
"""
a = 2
b = 4

print("Before Swapping: ",a,b)
temp = a
a = b
b = temp
print("After Swapping: ",a,b)
print("_"*100)

"""
9. Python program to solve this Pythagorous theorem.
Theorem : (a2 + b2 = c2)
"""
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

square_ab = ( a** 2) + ( b ** 2)
print("square_ab: ",square_ab)

c = math.sqrt(square_ab)
print("Pythagorous Answer(c): ",c)
print("_"*100)

"""
10. Python program to solve the given math formula.
Formula : (a + b)2 = a^2 + b^2 + 2ab
"""
input_a = float(input("Enter value a: "))
input_b = float(input("Enter value b: "))

#left side
LHS = (a + b) ** 2
print("LHS: ", LHS)

#right side
RHS = ( a ** 2) + ( b ** 2) + 2 * a * b
print("RHS: ",RHS)
print("Hence it is proved: LHS = RHS",LHS,'=',RHS)