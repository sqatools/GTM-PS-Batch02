
"""
if condition:
    code
else:
    code
"""
num1 = 100
num2 = 200
# Check num1 == mum2
if num1 == num2:
        print("Both variables have the same values")
else:
        print("Values are not same")
"""
Logical operators:

> : greater than operator
>= : greater than equal to
< : less than
<= : less than equal to
!= : not equal to
== : equal to operator
"""

"""
Input accepts the values as String only. 
We neet to convert the data type as per the requirements.
"""
"""
var1 = int(input("Please enter the first number :"))
var2 = int(input("Please enter the second number :"))

print(var1, type(var1), var2, type(var2))
"""

# greater than
"""
if var1 > var2:
    print("var1 has greater value", var1)
else:
    print("var2 has greater value", var2)
"""

# greater than equal
"""
if var1 >= var2:
    print("var1 has greater value", var1)
else:
    print("var2 has greater value", var2)
"""

# less than equal to
"""
if var1 <= var2:
    print("var1 has small value", var1)
else:
    print("var2 has small value", var2)
"""


# num1 = int(input("num1 value :"))
# num2 = int(input("num2 value :"))
# print("addition :", num1+num2)


######### multiple condition checking #######
"""
if cond1 and cond2:
   code
else:
   code
"""
a = 45
b = 67
c = 50
#   True and False : False
if c > a and c > b:
    print("c has grater value")
else:
    print("c does not have the greater value")

"""
AND OR Logical condition

False and False : False
True and False : False
True and True : True
False and True : False


False or False : False
True or False : True
True or True : True
False or True : True
"""

x = 500
y = 700
z = 501
#  False or False : False
if x == y or x == z:
    print("variables has equal value ")
else:
    print("variables does not have equal value")
