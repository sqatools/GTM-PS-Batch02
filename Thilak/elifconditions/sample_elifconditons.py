"""
if condition1:
   code
elif condition2:
   code
elif condition3:
   code
else:
    code
"""

a = 600
b = 500
c = 500
d = 50
e = 60

if a>b and a>c and a>d and a>e:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
else:
    print("no value is greater")
