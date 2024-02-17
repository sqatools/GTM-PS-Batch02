#(a – b)3 = a3 – 3a2b + 3ab2 – b3
a=int(input("value of a"))
b=int(input("value of b"))

LHS=(a-b)**3
RHS=a**3-3*a**2*b+3*a*b**2-b**3

print(LHS, RHS)