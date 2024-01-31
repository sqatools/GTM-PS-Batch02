print("hello")

#python variables and arithmatic operations

#1. Addition
var1=100
var2=200
add= var1+var2
print("addition = ", add)

#2. Sub
sub = var1 - var2
print("substraction: ",sub)

#multiplication

mul = var1 * var2
print("multiplication: ", mul)

#Division with single slash
var3 = 400
var4 = 3
div = var3 / var4
print("division single slash: ",div)

#Division with double slash
div_double_slash = var3//var4
print('division with double slash', div_double_slash)

#power operator **
#sqaure of 3

print("Sqaure of 3: ",var4**2)

""" Multiple number with string """
str1 = "Hello "
print(str1 * 3)
print("_" * 50)


""" (a + b)2 = a^2 + b^2 + 2ab """
a = 4
b = 7
#LHS
LHS = (a + b) ** 2
print("LHS: ",LHS)

#RHS
RHS = (a ** 2) + ( b ** 2) + 2 * (a*b)
print("RHS: ",RHS)
print("Hence: LHS = RHS")
print(LHS,'=',RHS)

print('_'*50)

#Get the type of variable
booleanTrue = True
booleanFalse = False
print('boolean type :')
print(type(booleanTrue),booleanTrue)
print(type(booleanFalse),booleanFalse)

print('_'*50)

