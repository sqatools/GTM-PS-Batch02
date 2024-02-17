#(a + b)3 = a3 + 3ab(a+b) + b3
a=int(input("value of a"))
b=int(input("value of b"))

LHS=(a+b)**3
RHS=a**3+3*a*b*(a+b)+b**3

print(LHS, RHS)