"""
if Condition:
    code
else:
    code
"""
a = 10
b = 20
if (a == b):
    print("These values are equal")
else:
    print("Sorry these values are not equal")

"""
Logical operator:
>: greater than equal
<= less than equal
<
>
>=
!=
==
"""


# Input accepts value as string only, we have to convert data type as per requirements.
class String:
    pass


# var1=int(input("Please enter the value1:"))
# print("Entered values is:", var1)

# ----------------Multi if condition --------------------#
print("-" * 50, "Multi if condition", "-" * 50)
"""
if cond1 and cond2
    code
else:
    code
"""

"""
#-------AND LOGICAL Condition---------#
FALSE and True = False
false and false= false
true and false= false
true and true= true


#------ OR Condition------------------#
True OR False = True
True or True= True
False or True= True
False or False = False
"""
# AND Operator
a = 10
b = 20
c = 30

if a == b and b == c:
    print("a and b,c values are same")
else:
    print("These values are not equal at all")

x = 100
y = 200
z = 300

if x == y or y == z:
    print("These values are equal")
else:
    print("These values are not equal")
