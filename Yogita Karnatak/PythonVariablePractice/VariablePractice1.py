var1 = 10
print(id(var1))

var2 = 20
print(id(var2))

var3 = 10
print(id(var3))
# if multiple variable holding same value then their memory address will be same.

# Rules to define variable name
 # Variable name should not start with number
   #2var = 600 : Invalid
   #Var345 = 700 : Valid
   #V1a4r = 500 : Valid

 # There should not be space in variable name.
   # Var 1 = 900 : Invalid
   # Var_1 = 900 : Valid
   # abc_pqr = "Hello" : Valid

 # Python is case sensitive language, variable name with upper case & lower case will be different.

"""
Multiple comment  with triple quote.
name = "Rahul"
Name = "Kapil"
NAME = "Raj"
nAmE = "Gaurav"
print(name, Name, NAME, nAmE)
"""
# Assign multiple values to multiple variables
p, q, r = 100, 200, 300
print("Value of p:", p)
print("Value of q:", q)
print("Value of r:", r)

# Assign single value to multiple variables
x=y=z= 100
print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)


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
