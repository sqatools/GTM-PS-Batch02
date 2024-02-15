
#Formula : (a - b)2 = a^2 + b^2 - 2ab

a = 2
b = 3
#LHS
LHS = (a - b)**2
print("LHS: ", LHS)

#RHS
RHS = (a**2) + (b**2) - (2 * a * b)
print("RHS: ", RHS)

#Formula : a2 – b2 = (a-b)(a+b)

a = 2
b = 3
LHS = a**2 - b**2
print("LHS: ", LHS)

#RHS
RHS = (a-b) * (a+b)
print("RHS: ", RHS)

#Formula : (a + b)3 = a3 + 3ab(a+b) + b3

a = 2
b = 3
LHS = (a+b)**3
print("LHS: ", LHS)

#RHS
RHS = a**3 + (3*a*b) * (a+b) + b**3
print("RHS: ", RHS)


#Formula : (a – b)3 = a3 – 3a2b + 3ab2 – b3

a = 3
b = 2
LHS = (a-b)**3
print("LHS: ", LHS)

#RHS
RHS = a**3 - (3*a*2*b) + (3*a*b*2) - b**3
print("RHS: ", RHS)

#program to calculate the area of the square.
#Formula : area = a*a

a= 2
area = a*a
print("area of the square is: ", area)

# program to calculate the area of a circle.
'''Formula = PI*r*r
r = radius
PI = 3.14'''

r = 2.5
PI = 3.14
res = PI * r * r
print("area of a circle is: ", res)

# program to calculate the area of a cube.
#Formula = 6*a*a

a= int(input("enter the value: "))
area_of_cube = 6 * a * a
print("area of cube is: ", area_of_cube)

#program to calculate the area of the cylinder.
#Formula = 2*PI*r*h + 2*PI*r*r

r = 2.5
h = 2
area_of_cylinder = 2*PI*h*r + 2 *PI*r*r
print("area of cylinder is: ", area_of_cylinder)

#Python program to calculate simple interest.
'''
Formula = P+(P/r)*t
P = Principle Amount
r = Anual interest rate
t = time
'''

P = int(input("Enter the priniciple amount: "))
r = int(input("enter the Anual interest rate: "))
t = int(input("enter the time: "))

interest = P + (P/r)* t
print("interest: ", interest)