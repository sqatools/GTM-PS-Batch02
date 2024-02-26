"""
21). Python program to check whether the given number is positive or negative and even or odd.
Input = 26
Output = The given number is positive and even
"""
input1 = int(input("Enter number to check +ve/-ve and even/odd: "))

if input1 > 0:
    if input1 % 2 == 0:
        print("21. The given number is positive and even")
    else:
        print("21. The given number is positive and odd")
else:
    if input1 % 2 == 0:
        print("21. The given number is negative and even")
    else:
        print("21. The given number is negative and odd")
print("_"*100)

"""
22. Python program to print the largest number from two numbers.
Input:
25, 63
Output = 63
"""
print("Problem 22: Python program to print the largest number from two numbers")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("22.", num1, "is the largest number among two")
else:
    print("22.", num2, "is the largest number among two")
print("_"*100)

"""
23.  Python program to check whether a given character is uppercase or not.
Input = A
Output = The given character is an Uppercase
"""
input_str = "M"
print("23. character is uppercase or not: ",input_str, ':', input_str.isupper())
print("_"*100)

"""
24). Python program to check whether the given character is lowercase or not.
Input = c
Output = True
"""
input_str = "A"
print("24. character is lowercase or not: ", input_str, ":", input_str.islower())
print("_"*100)

"""
25.Python program to check whether the given number is an integer or not.
Input = 54
Output = True
"""

input_num = 54
print("25. the given number is an integer: ", isinstance(input_num,int))
print("_"*100)

"""
26). Python program to check whether the given number is float or not.
Input = 12.6
Output = True
"""

input_num = 12.6
print("26. the given number is an float: ", isinstance(input_num, float))

#sol2

if type(input_num) == float:
    print('26. ', True)
else:
    print('26. ', False)
print("_"*100)

"""
27). Python program to check whether the given input is a string or not.
Input = ‘sqatools’
Output = True
"""

input_str = "sqatools"

print("27. given input is string or not: ", isinstance(input_str,str))
print("_"*100)

"""
28.  Python program to print all the numbers from 10-15 except 13
Output:
10
11
12
14
"""
print("28. Print all the numbers from 10-15 except 13")
for i in range(10, 15):
    if i == 13:
        continue
    else:
        print(i)
print("_"*100)

"""
29. Python program to find the electricity bill. According to the following conditions:
Up to 50 units rs 0.50/unit
Up to 100 units rs 0.75/unit
Up to 250 units rs 1.25/unit
above 250 rs 1.50/unit
an additional surcharge of 17% is added to the bill
Input = 350
Output = 438.75
"""

"""
30. Python program to check whether a given year is a leap or not.
Input = 2000
Output = The given year is a leap year
"""

input_year = 2005
if (input_year % 4 == 0 and (input_year % 100 != 0 or input_year % 400 == 0)):
    print("30. The given year is a leap year")
else:
    print("30. The given year is not a leap year")