#Python Program to add two integer values
a = 2
b = 3
print("Addition of two numbers;", a+b)

#python Program to subtract two integer values
a = 12
b = 3
print("subtraction of two numbers;", a-b)

#python Program to multiply 2 values
a = 2
b = 3
print("Multiplication of two numbers;", a*b)

#Python program to repeat a given string 5 times

char = 'He'
print(char*5)

#Python program to get the Average of given numbers

a = 2
b = 3
c = 4
print("average of numbers:",(a+b+c)/2)

#median of odd number

x = [4,5,7,6,9]
x.sort()
n = (len(x))/2
print("median of odd no:", x[int(n)])

#sq and cube of given no

a = 2
print("square of a is:",a**2)
print("cube of a is:",a**3)

#interchange values between variables.
a = 4
b = 8

a,b = b,a

print(a)
print(b)

#pythogorous theorem (a2 + b2 = c2)
a = 2
b = 3
RHS = (a**2)+(b**2)
LHS = (a**2)+(b**2)
print(LHS, "=", RHS)

#program to solve the given math formula.
#Formula : (a + b)2 = a^2 + b^2 + 2ab


a = 2
b = 3
#LHS
LHS = (a + b)**2
print("LHS: ", LHS)

#RHS
RHS = (a**2) + (b**2) +(2 * a * b)
print("RHS: ", RHS)
