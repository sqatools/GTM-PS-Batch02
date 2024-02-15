"""
SQA Tools
Python If-Else Programs
11 to 20
"""
"""
    11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
"""
num1 = int(input("Enter Number divided by 2 or 3: "))
if (num1 % 2 ) ==0:
    print("Number is divisible by 2 : Sqaure of: ",num1, '=', num1**2)
elif (num1 % 3 == 0):
    print("Number is divisible by 3 : Cube of: ",num1, '=', num1**3)
else:
    print("Number is not divisible by 2 nor by 3")
print("_"*100)

"""
 12). Python program to describe the interview process.
"""

"""
13.Python program to determine whether a given number is available in the list of numbers or not.
"""
input_list = [10,20,30,40,50,60,78,8899]
num2 = int(input("Enter Number to check present in list or not: "))

if num2 in input_list:
    print("Present in list")
else:
    print("Not Present in list")
print("_"*100)

"""
14). Python program to find the largest number among three numbers.
"""
input_num1 = float(input("Enter first to check largest: "))
input_num2 = float(input("Enter second to check largest: "))
input_num3 = float(input("Enter third to check largest: "))

if input_num1 > input_num2 and input_num1 > input_num3:
    print("A is largest: ",input_num1)
elif input_num2 > input_num1 and input_num2 > input_num3:
    print("B is largest: ",input_num2)
else:
    print("C is largest: ",input_num3)
print("_"*100)

"""
15. Python program to check any person eligible to vote or not
age > 18+ : eligible
age < 18: not eligible
"""

age = int(input("Enter age to check eligiblity: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
print("_"*100)

"""
16). Python program to check whether any given number is a palindrome.
Input: 121
Output: palindrome
"""

#convert number into string
num_input = 121
str1 = str(num_input)
print('slicing str: ',str1[::-1])
print("_"*100)

"""
17). Python program to check if any given string is palindrome or not.
Input: ‘jaj’
output = palindrome
"""

input_str = 'madhuri'
slic_str = input_str[::-1]
print("reversed string: ",slic_str)
if input_str == slic_str:
    print("string is palindrom: LHS = RHS : ",input_str,'=',slic_str)
print("_"*100)

"""
18). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
Input = Enter marks: 45
Output = Pass
"""
marks = 45
if marks >= 35:
    print("Student has passed the exam")
else:
    print("Student has failed in the exam")
print("_"*100)

"""
19). Python program to check whether the given number is positive or not.
Input = 20
Output = True
"""
positive_input = 20

if positive_input > 0:
    print("Number is positive")
else:
    print("Number is not positive")
print("_"*100)
"""
20). Python program to check whether the given number is negative or not.
Input = -45
Output = True
"""

negative_input = -45
if negative_input < 0 :
    print("Number is negative")
else:
    print("Number is not negative")