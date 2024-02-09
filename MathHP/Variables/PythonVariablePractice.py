#No semicolon at the end
#No data type/return type required to declare variables
#To print id address of the variable
#Same variable name can be given, duplication allowed

var1 = 10
print(id(var1))  #140707278502616

var2 = 20
print(id(var2))  #140707278502936

#If multiple variables holding same value then their memory address will be same

var3 = 10
print(id(var3))  #140707278502616


#Rules to define variable name

#Variable is a container holding value
#Same value of different variables hold same memory address

#1) Variable name should not strat with number only alphanumeric

#2var1 = 600; invalid
#var123 = 700; valid
#abc_pqr = 300; valid


#2)No space in variable name
#var 1 = 4; invalid

#3)Underscore is allowed, no other special characters allowed
#var_12 = 200; valid
#var$% = 3; invalid

#4)Python is case sensitive language
name = "Rahul"
Name = "rahul"

print(name,Name)

#Assign multiple values to multiple variables at a time

p,q,r = 600,700,800
print("Value of p :", p)
print("Value of q :", q)
print("Value of r :", r)

#Assign single value to multiple variables

x=y=z = 100
print("value of x :", x)
print("value of y :", y)
print("value of z :", z)

#Mathematical operation
"""
+ = Plus operator                                   #Multiline comments, not taken by Python been ignored
- = Minus operator
* = Multiplication operator
/ = Division with single slash
// = Division with double slash
** = Power operator
"""

#Addition of 2 numbers

var1 = 2000
var2 =300
var3 = var1 + var2
print("Addition of two numbers : ",var3)

#Subtraction
sub = var1-var2
print("Subtraction of two numbers : ",sub)

#Multiplication
mul = var1*var2
print("Multiplication of two numbers : ", mul)

#Division with /
div = var1/var2
print("Division of two numbers : ",div)

#Division with //   gives only quotient no decimal values , only whole numbers
div = var1//var2
print("Division of two numbers with // : ",div) #same variable name div

num1 = 6
print("square of value : ", num1**2)   #power num1*num1
print("cube of value : ",num1**3)      #power 3 num1*num1*num1

#Multiple number with String
str1 = "Hello"
print(str1*3)   #HelloHelloHello

print("_"*50)              #Any special characters ,String can be multiplied

#Solve quadratic equation
#(a+b)2 = a^2 + b^2 + 2ab
a=4
b=7
#LHS

LHS = (a+b)**2            #Power means **
print("LHS : ", LHS)

#RHS
RHS = a**2 + b**2 +2*a*b
print("RHS : ", RHS)



