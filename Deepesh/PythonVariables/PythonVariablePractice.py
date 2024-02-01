a = 20
# a : Variable
# = : Assignment Operator
# 20 : Data

print(a)
print(id(a))
b = 500

c = a + b
# + : Plus operator
print(c, id(c))

# If we have 2 different variable with same value, then their
# memory address will be same.
p = 50
q = 50
print(id(p), id(q))

# Assign multiple values to multiple variables.
a, b, c = 50, 'Python', 70
print("Value of a:", a, id(a))
print("b:", b, id(b))
print("c:", c, id(c))
print("Hello Good Morning")

# Assign Single Values to Multiple Variables
x = y = z = 700

print("Value of x :", x, id(x))
print("Value of y :", y, id(y))
print("Value of z :", z, id(z))

# Rules to defined variable name
# -> We start variable with underscore or any character
# -> Number as prefix it not allowed
# -> Space in variable name is not allowed.
# -> We defined any long variable
# -> Special character is not allowed in the variable name.

var1 = 50
_var2 = 60
python_variable_name = 'Learning Programming'
python_variable_543253452454 = 'Learning Programming'
# 2num = 500 : wrong name
# 40var = 600 : wrong name
# num1 abc = 900 : wrong name
# var$xyz = 500 : wrong name

# Mathematical Operation on variables
# + : Plus Operator
# - : Minus Operator
# * : Multiplication Operator
# / : Division Operator1
# // : Division Operator2
# ** : Power Operator
# == : Equal to Operator

# Python Case Sensitive Programming Language
name = 'Hello'
Name = "Python"
NAME = 'Programming'

print("name:", name)
print("Name:", Name)
print("NAME:", NAME)

# addition
num1 = 50
num2 = 60

print("addition:", num1 + num2)
# subtraction
print("subtract :", num1 - num2)
num3 = num1 - num2
print(num3)

# multiplication
print("Multiplication :", num1 * num2)

# Visible
x = 50
y = 4

# divide with single slace /
result = x / y
print("result :", result, type(result))

# divide with double slace //
result2 = x // y
print("result2:", result2, type(result2))

# Power Operator
# 2 power 3

print("2 power 3:", 2 ** 3)
print("8 power 2:", 8 ** 2)
print("5 power 3 :", 5 ** 3)

# equal to operator ==

var1 = 50
var2 = 60
print(var1 == var2)  # False

var3 = 60
var4 = 60
print(var3 == var4)  # True
