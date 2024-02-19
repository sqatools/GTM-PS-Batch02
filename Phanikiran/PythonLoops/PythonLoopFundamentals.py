"""
- for range(initial value, end value, different value)
- It will print the value till end value-1 eg. if we try to iterate (1 10 2) -- It pritnts till 9 with 2 different value.
- If we don't mention the difference value then by default its 1.
- If we don't mention the initiatl value then by default its 0.
"""
from math import factorial

for i in range(2, 10, 1):  # (initial value, end value, difference value)
    print(i)

# Without difference value where default is 1
for i in range(1, 10):
    print(i, end="")  # 1 2 3 4 5 6 7 8 9

# Range with only two parameters
# range(initial value, end value)
for j in range(5):
    print(j)
    print("*" * 5)

# Program to print  table for a given number.ex.5
num = 5
for i in range(1, 11):
    print(i, "*", num, "=", i * num)

print("*" * 100)
num = 6
for i in range(1, 11):
    print(i * num)

# Printing values in reverse order
for j in range(10, 0, -1):
    print(j)
print()

# Factorial of a number
"""fact = 1
name = input("Enter the number\n")
for i in range(name, 0, -1):
    fact = fact * 1
print("The factorial of given number", num1, fact)
"""

# Continue and break statement
for i in range(10):
    if i == 8:
        break
    else:
        print(i)
print("*" * 500)
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

print("*" * 500)

# Find out palindrome or not
num = "HEH"
rev_num = str(num)[::-1]

if rev_num == num:
    print("It is a palindrome ")
else:
    print("It is not Palindrome")

# Find whether given number is integer or not
n = 10
if isinstance(n, int):
    print("This is an integer")
else:
    print("This is not integer")

print("*" * 400)

# Applying loop on list and displaying data according data type.

list1 = ['33', "phanikiran", '34', True, '23.5']
for i in list1:
    if isinstance(i, int):
        print("This value is integer", i)
    else:
        print("This is not a integer")
